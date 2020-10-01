from flask import request, abort
from flask_restful import Resource
from auth import requires_auth
from models import User, Product, Category


class Products(Resource):
    def get(self, product_id=None):
        if product_id is not None:
            return self.get_product_by_id(product_id)
        try:
            products = [product.format() for product in Product.query.all()]
        except Exception:
            abort(500)
        if products:
            return {"success": True, "products": products}
        else:
            abort(404)

    def get_product_by_id(self, product_id):
        try:
            product = Product.query.get(product_id)
        except Exception:
            abort(500)
        if product:
            return {"success": True, "product": product.format()}
        else:
            abort(404)

    def post(self):
        payload = requires_auth(request.headers.get("Authorization"), "post:products")
        try:
            data = request.get_json()
            seller = User.query.filter_by(user_id=payload["sub"]).one_or_none()
            name, price = data["name"], data["price"]
            assert all({name, price, seller_id})
            assert seller is not None
        except Exception:
            abort(400)

        try:
            category_id = data.get("category_id")
            quantity = data.get("quantity")
            product = Product(name, price)
            product.seller = seller

            if category_id:
                category = Category.query.get(category_id)
                if category:
                    product.category = category
            if quantity:
                product.quantity = quantity

            product.insert()
        except Exception:
            abort(422)
        finally:
            product_id = product.id

        return {"success": True, "product_id": product_id}

    def patch(self, product_id):
        payload = requires_auth(request.headers.get("Authorization"), "patch:products")
        try:
            product = Product.query.get(product_id)
        except Exception:
            abort(500)
        if not product:
            abort(404)

        try:
            data = request.get_json()
            name = data.get("name")
            price = data.get("price")
            quantity = data.get("quantity")
            category_id = data.get("category_id")
        except Exception:
            abort(400)

        try:
            if name:
                product.name = name
            if price:
                product.price = price
            if quantity:
                product.quantity = quantity
            if category_id:
                product.category = Category.query.get(category_id)
            product.update()
        except Exception:
            abort(422)

        return {"success": True, "product": product.fornat()}

    def delete(self, product_id):
        payload = requires_auth(request.headers.get("Authorization"), "delete:products")
        try:
            product = Product.query.get(product_id)
        except Exception:
            abort(500)

        if not product:
            abort(404)

        try:
            product.delete()
        except Exception:
            abort(422)

        return {"success": True, "product_id": product_id}
