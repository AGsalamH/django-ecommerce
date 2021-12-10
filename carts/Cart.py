from django.http.request import HttpRequest
from products.models import Product


class Cart:

    def __init__(self, request:HttpRequest):
        self.session = request.session
        cart = self.session.get('cart')
        if 'cart' not in self.session:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self, product:Product, qty:int):
        '''
        Add and Update cart items
        '''
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {
                'price': float(product.price),
                'qty': int(qty)
            }
        self.save()

    def delete(self, product_id:int):
        '''
        Delete cart item
        '''
        if str(product_id) in self.cart:
            self.cart.pop(str(product_id))
            self.save()

    def save(self):
        '''
        Save session to DB
        '''
        self.session.modified = True