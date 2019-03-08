from decimal import Decimal
from django.conf import settings
from home.models import House

class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
        # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

        def add(self, house, quantity=1, update_quantity=False):
            """
            Add a product to the cart or update its quantity.
            """
            house_id = str(house.id)
            if house_id not in self.cart:
                self.cart[house_id] = {'quantity': 0, 'price': str(house.price)}
            if update_quantity:
                self.cart[house_id]['quantity'] = quantity
            else:
                self.cart[house_id]['quantity'] += quantity
                self.save()

        def save(self):
            # update the session cart
            self.session[settings.CART_SESSION_ID] = self.cart
            # mark the session as "modified" to make sure it is saved
            self.session.modified = True

        def remove(self, house):
            """
            Remove a product from the cart.
            """
            house_id = str(house.id)
            if house_id in self.cart:
                del self.cart[house_id]
                self.save()



        def __iter__(self):
            """
            Iterate over the items in the cart and get the houses
            from the database.
            """
            house_ids = self.cart.keys()
            # get the house objects and add them to the cart
            houses = House.objects.filter(id__in=product_ids)
            for house in houses:
                self.cart[str(house.id)]['house'] = house
            for item in self.cart.values():
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * item['quantity']
                yield item
        def __len__(self):
            """
            Count all items in the cart.
            """
            return sum(item['quantity'] for item in self.cart.values())

        def get_total_price(self):
            return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

        def clear(self):
            # remove cart from session
            del self.session[settings.CART_SESSION_ID]
            self.session.modified = True
