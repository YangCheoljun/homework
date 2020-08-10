from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.dbsparta

@app.route('/')
def home():
    result = render_template('index.html')

    return result

@app.route('/order', methods=['GET'])
def get_order():
    orders = list(db.shopping.find({}, {'_id': 0}))
    print(orders)
    result = jsonify({
        'result': 'success',
        'msg': 'GET을 성공했습니다.',
        'orders': orders,
    })
    return result

@app.route('/order', methods=['POST'])
def post_order():
    name_receive = request.form['name']
    count_receive = request.form['count']
    phone_receive = request.form['phone']
    address_receive = request.form['address']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'phone': phone_receive,
        'address': address_receive,
    }
    db.shopping.insert_one(doc)

    result = jsonify({
        'result': 'success',
        'msg': 'Post를 성공했습니다.'
    })

    return result

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)