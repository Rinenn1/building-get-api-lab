#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries', methods=["GET"])
def bakeries():
    bakeries = [bakery.to_dict() for bakery in Bakery.query.all()]
    
    response = make_response(
        jsonify(bakeries),
        200
    )
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()

    baker = bakery.to_dict()

    response = make_response(
        baker,
        200
    )

    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked = BakedGood.query.order_by(BakedGood.price.desc()).all()

    baked_goods = [bakes.to_dict() for bakes in baked]

    response = make_response(
        jsonify(baked_goods),
        200
    )

    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked = BakedGood.query.order_by(BakedGood.price.desc()).first()

    expense_baked = baked.to_dict()

    response = make_response(
        expense_baked,
        200
    )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
