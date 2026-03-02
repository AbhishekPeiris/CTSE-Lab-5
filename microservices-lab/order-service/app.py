from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
orders = []
id_counter = 1

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def place_order():
    global id_counter
    order = request.get_json()
    order['id'] = id_counter
    order['status'] = 'PENDING'
    id_counter += 1
    orders.append(order)
    return jsonify(order), 201

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    for order in orders:
        if order['id'] == id:
            return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
