import json, os

from saleapp import app
from saleapp.models import Category, Product


# def read_json(path):
#     with open(path, 'r') as f:
#         return json.load(f)


def load_categories():
    # return read_json(os.path.join(app.root_path, 'data/categories.json'))
    return Category.query.all()

def load_products(cate_id=None, kw=None, page=1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))

    return query.all()


# def get_product_by_id(product_id):
#     products = read_json(os.path.join(app.root_path, 'data/products.json'))
#
#     return [p for p in products if (p['id'] == product_id)][0]
