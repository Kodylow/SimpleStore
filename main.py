from flask import Flask, render_template
import random
from hashlib import sha256

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/store')
def market_page():
    items = [{
        'id': 1,
        'name': 'Phone',
        'barcode': sha256(random.randbytes(8)).hexdigest(),
        'price': '$' + random.randint(1, 100)
    }, {
        'id': 2,
        'name': 'Laptop',
        'barcode': sha256(random.randbytes(8)).hexdigest(),
        'price': '$' + random.randint(1, 100)
    }, {
        'id': 3,
        'name': 'Keyboard',
        'barcode': sha256(random.randbytes(8)).hexdigest(),
        'price': '$' + random.randint(1, 100)
    }]
    return render_template('store.html', items=items)


app.run(host='0.0.0.0', port=81, debug=True)
