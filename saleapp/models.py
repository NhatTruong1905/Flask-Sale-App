from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, Text, Enum
from saleapp import db, app
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from enum import Enum as UserEnum
from sqlalchemy import Text


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    avatar = Column(String(1000),
                    default='https://res.cloudinary.com/dice7ntoz/image/upload/v1764581674/avatar-facebook-mac-dinh-10_fqblxm.jpg')
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(20), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, default=0)
    image = Column(String(1000),
                   default="https://res.cloudinary.com/dice7ntoz/image/upload/v1764583917/licensed-image_zqumzq.jpg")
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # import hashlib
        #
        # u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role=UserRole.ADMIN)
        # db.session.add(u)
        # db.session.commit()

        # c1 = Category(name='Mobile')
        # c2 = Category(name='Table')
        # c3 = Category(name='Laptop')
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        #
        # products = [{
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        #     "category_id": 1
        # },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAML: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAML: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAML: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #         "category_id": 1,
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAML: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #         "category_id": 1
        #     }]
        # products = [
        #     {
        #         "name": "Samsung Galaxy S23",
        #         "description": "Samsung, 128GB, RAM: 8GB, Android 13",
        #         "price": 20000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764582389/samsung-galaxy-s23-plus-kem-1-750x500_ih6nsg.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "iPhone 15 Pro Max",
        #         "description": "Apple, 128GB, RAM: 6GB, iOS16",
        #         "price": 35000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764582843/iphone-15-pro-max-blue-thumbnew-600x600_uv6u7s.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "iPad Mini 6",
        #         "description": "Apple, 64GB, RAM: 4GB",
        #         "price": 15000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764582878/ipad-mini-6-wifi-starlight-1-600x600_uznk39.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Samsung Galaxy Tab S7",
        #         "description": "Samsung, 128GB, RAM: 6GB",
        #         "price": 22000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764583007/samsung-galaxy-tab-s7-gold-new-600x600_scsjid.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "MacBook Pro 14",
        #         "description": "Apple, i9, 16GB RAM, 1TB SSD",
        #         "price": 50000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764583011/macbook-pro-14-inch-m4-pro-bac-600x600_y2igzk.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "Dell XPS 13",
        #         "description": "Dell, i7, 16GB RAM, 512GB SSD",
        #         "price": 30000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764583070/dell-xps-13-9350-ultra-7-258v-pp9h1-thumb-638920701947915998-600x600_ew9zoa.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "Google Pixel 8",
        #         "description": "Google, 128GB, RAM: 8GB, Android 14",
        #         "price": 23000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764583084/google-pixel-8-600x600_vjz4at.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "OnePlus 11",
        #         "description": "OnePlus, 128GB, RAM: 8GB, Android 13",
        #         "price": 18000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764583200/oneplus-11-600x600_sxcnau.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Microsoft Surface Pro 8",
        #         "description": "Microsoft, i7, 16GB RAM, 256GB SSD",
        #         "price": 40000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764583290/surface-pro-8-man-hinh-13-inch-_1920x1080-800-resize_c92jld.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "Samsung Galaxy Book3",
        #         "description": "Samsung, i5, 8GB RAM, 512GB SSD",
        #         "price": 28000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764583363/c-140223-230059-800-resize_siwnb7.jpg",
        #         "category_id": 3
        #     }
        # ]
        # products = [
        #     {
        #         "name": "Xiaomi 13 Pro",
        #         "description": "Xiaomi, 256GB, RAM: 12GB, Snapdragon 8 Gen 2",
        #         "price": 23000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585271/xiaomi-13-pro-thumb-1-2-600x600_s8njgp.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Sony Xperia 1 V",
        #         "description": "Sony, 256GB, RAM: 12GB, 4K OLED Display",
        #         "price": 29000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585275/product-315601-180923-103842-600x600_b9wjhl.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Oppo Find N3 Flip",
        #         "description": "Oppo, 256GB, RAM: 12GB, Foldable",
        #         "price": 22990000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585296/oppo-find-n3-flip-hong-thumb-1-600x600_k0cpph.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Asus ROG Phone 7",
        #         "description": "Asus, 512GB, RAM: 16GB, Gaming Phone",
        #         "price": 25000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585367/asus-rog-phone-7-pro-600x600_jvcsvx.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "iPad Air 5 M1",
        #         "description": "Apple, 64GB, WiFi, Chip M1 mạnh mẽ",
        #         "price": 14500000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585385/ipad-air-5-wifi-cellular-tim-thumb-600x600_lsuxok.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Xiaomi Pad 6",
        #         "description": "Xiaomi, 128GB, RAM: 8GB, 144Hz Display",
        #         "price": 8990000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585392/xiaomi-mi-pad-6s-pro-grey-thumb-600x600_j52up0.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Lenovo Tab P11 Pro",
        #         "description": "Lenovo, 128GB, RAM: 6GB, OLED Screen",
        #         "price": 10500000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585511/P3g3MDQ2MQ_x5gfpz.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Asus ROG Strix G16",
        #         "description": "Asus, i7-13650HX, RAM 16GB, RTX 4060, 512GB SSD",
        #         "price": 32990000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585542/asus-rog-strix-g16-g614ju-i7-n3509w-170225-114540-460-600x600_it5yua.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "HP Spectre x360",
        #         "description": "HP, i7-1355U, RAM 16GB, 1TB SSD, Cảm ứng xoay gập",
        #         "price": 42000000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585548/hp-spectre-x360-14-eu0050tu-ultra-7-a19blpa-638763555305898173-600x600_v8dpwi.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "Acer Swift 3",
        #         "description": "Acer, i5-1240P, RAM 16GB, 512GB SSD",
        #         "price": 16990000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585930/acer-swift-sf315-52-38yq-i3-8130u-4gb-1tb-156f-win-21-208863-600x600_ifmmfx.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "MSI Katana 15",
        #         "description": "MSI, i7-13620H, RAM 16GB, RTX 4050, 144Hz",
        #         "price": 27990000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764585979/msi-katana-15-b13udxk-i5-2410vn-638895766162144479-600x600_sarf76.jpg",
        #         "category_id": 3
        #     }, {
        #         "name": "Lenovo LOQ 15IRH8",
        #         "description": "Lenovo, Core i5-12450H, RAM 16GB, SSD 512GB, RTX 2050 4GB, 144Hz",
        #         "price": 18500000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764586008/lenovo-loq-gaming-15irh8-i7-82xv00qxvn-thumb-600x600_lpvdoj.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "Lenovo LOQ 15IAX9",
        #         "description": "Lenovo, Core i5-13420H, RAM 16GB, SSD 512GB, RTX 4050 6GB, Màn chuẩn màu",
        #         "price": 24990000,
        #         "image": "https://res.cloudinary.com/dice7ntoz/image/upload/v1764586067/lenovo-loq-15iax9e-i5-83lk0079vn-thumb-638828190971476549-600x600_zl6fdn.jpg",
        #         "category_id": 3
        #     },
        # ]
        #
        # for p in products:
        #     pro = Product(**p)
        #     db.session.add(pro)
        #
        # db.session.commit()
