from flask import Flask
import jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
@app.route('/api/v1/products')
def return_json():
    return jsonify({'PRODUCTS' : {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
}
})