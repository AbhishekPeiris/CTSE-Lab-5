from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
payments = []
id_counter = 1

@app.route('/payments', methods=['GET'])
def get_payments():
    return jsonify(payments)

@app.route('/payments/process', methods=['POST'])
def process_payment():
    global id_counter
    payment = request.get_json()
    payment['id'] = id_counter
    payment['status'] = 'SUCCESS'
    id_counter += 1
    payments.append(payment)
    return jsonify(payment), 201

@app.route('/payments/<int:id>', methods=['GET'])
def get_payment(id):
    for payment in payments:
        if payment['id'] == id:
            return jsonify(payment)
    return jsonify({"error": "Payment not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)
