from flask_admin import Admin
from saleapp import app, db
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Category, Product

admin = Admin(app=app, name="Product's Admin")
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
