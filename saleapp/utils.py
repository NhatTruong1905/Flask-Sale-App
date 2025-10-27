import json, os

from saleapp import app


def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))


def load_products(cate_id=None, keyword=None, from_price=None, to_price=None):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))

    if cate_id:
        products = [p for p in products if p['category_id'] == int(cate_id)]

    if keyword:
        products = [p for p in products if p['name'].lower().find(keyword.lower()) > 0]

    if from_price:
        products = [p for p in products if p['price'] >= float(from_price)]

    if to_price:
        products = [p for p in products if p['price'] <= float(to_price)]

    return products


def get_product_by_id(product_id):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))

    return [p for p in products if (p['id'] == product_id)][0]
