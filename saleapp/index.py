from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from saleapp import app
from flask import render_template
import utils

@app.route('/')
def home():
    cates = utils.load_categories()
    return render_template('index.html', categories=cates)


@app.route('/products')
def product_list():
    products = utils.load_products()
    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
