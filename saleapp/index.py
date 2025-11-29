from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from saleapp import app, utils, login
from flask import render_template, request, redirect, jsonify
from flask_login import login_user, logout_user
import math
from saleapp.utils import add_user
from sqlalchemy.exc import PendingRollbackError


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


@app.route('/register', methods=['POST'])
def register_process():
    data = request.form

    password = data['password']
    confirm = data['confirm']
    if password != confirm:
        err_msg = 'Mật khẩu không khớp'
        return render_template('register.html', err_msg=err_msg)
    try:
        add_user(name=data.get('name'), username=data.get('username'), password=data.get('password'),
                 avatar=request.files.get('avatar'))
        return redirect('/login')
    except Exception as ex:
        return render_template('register.html', err_msg=str(ex))


@app.route('/logout')
def Logout_process():
    logout_user()
    return redirect('/login')


@app.route('/login', methods=['POST'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')
    user = utils.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    next = request.args.get('next')
    return redirect(next if next else '/admin')


@app.route('/api/carts', methods=['POST'])
def add_to_cart():
    print(request.json)


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
