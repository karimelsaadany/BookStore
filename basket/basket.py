from store.models import Product
from decimal import Decimal


class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherted or overriden, as necessary
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, productqty):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['productqty'] = productqty
        else:
            self.basket[product_id] = {'price': str(product.price), 'productqty': productqty}
        self.save()

    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
        self.save()
    
    def update(self, product, productqty):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['productqty'] = productqty
        self.save()

    def __iter__(self):
        product_ids  =self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product
        
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['productqty']
            yield item

    def __len__(self):
        return sum(item['productqty'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['productqty'] for item in self.basket.values())
    
    def save(self):
        self.session.modified = True