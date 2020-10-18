from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Book"
    },
    {
        "id": 2,
        "name": "lap"
    }
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/products', method=['POST'])
def put_products():
    

if __name__ == "__main__":
    app.run(debug=True)