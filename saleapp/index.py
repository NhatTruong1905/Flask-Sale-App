from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from saleapp import app, utils, login
from flask import render_template, request, redirect
from flask_login import login_user, logout_user
import math


@app.route('/')
def home():
    products = utils.load_products(cate_id=request.args.get('category_id'), kw=request.args.get('kw'),
                                   page=int(request.args.get('page', 1)))

    return render_template('index.html', products=products,
                           page=math.ceil(utils.count_products() / app.config["PAGE_SIZE"]))


@app.route('/login')
def login_view():
    return render_template('login.html')


@app.route('/register')
def register_view():
    return render_template('register.html')


@app.route('/logout')
def Logout_process():
    logout_user()
    return redirect('/login')


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

@app.route('/login', methods=['POST'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')
    user = utils.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    next = request.args.get('next')
    return redirect(next if next else '/admin')


@app.context_processor
def common_responses():
    return {
        'categories': utils.load_categories()
    }


@login.user_loader
def load_user(id):
    return utils.get_user_by_id(id)


if __name__ == '__main__':
    from saleapp import admin

    app.run(debug=True)
