import json, os

from saleapp import app
from saleapp.models import Category, Product, User
import hashlib
from saleapp import app


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

    if page:
        start = (page - 1) * app.config['PAGE_SIZE']
        query = query.slice(start, start + app.config['PAGE_SIZE'])

    return query.all()

def count_products():
    return Product.query.count()

def get_user_by_id(id):
    return User.query.get(id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username == username, User.password == password).first()
