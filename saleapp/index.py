from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from saleapp import app, utils
from flask import render_template, request
import utils


@app.route('/')
def home():
    categories = utils.load_categories()
    products = utils.load_products(cate_id=request.args.get('category_id'), kw=request.args.get('kw'),
                                   page=request.args.get('page'))

    return render_template('index.html', categories=categories, products=products)


# @app.route('/products')
# def product_list():


# cate_id = request.args.get('category_id')
# keyword = request.args.get('keyword')
# from_price = request.args.get('from_price')
# to_price = request.args.get('to_price')
# products = utils.load_products()


# return render_template('products.html', products=products)


# @app.route('/products/<int:product_id>')
# def product_detail(product_id):
#     product = utils.get_product_by_id(product_id)
#     return render_template('product_detail.html', product=product)


if __name__ == '__main__':
    from saleapp import admin

    app.run(debug=True)
