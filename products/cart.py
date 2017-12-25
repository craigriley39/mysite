from decimal import Decimal
from django.conf import settings
from .models import Product

class Cart(object):

    """
    A cart that lives in the session.
    """
    def __init__(self, session, session_key=None):
        self._items_dict = {}
        self.session = session
        self.session_key = session_key or carton_settings.CART_SESSION_KEY
            # If a cart representation was previously stored in session, then we
        if self.session_key in self.session:
            # rebuild the cart object from that serialized representation.
            cart_representation = self.session[self.session_key]
            ids_in_cart = cart_representation.keys()
            products_queryset = self.get_queryset().filter(pk__in=ids_in_cart)
            for product in products_queryset:
                item = cart_representation[str(product.pk)]
                self._items_dict[product.pk] = CartItem(
                    product, item['quantity'], Decimal(item['price'])
                )

    def get_queryset(self):
        #product_model = self.get_product_model()
        queryset = Product.objects.all()
        queryset = self.filter_products(queryset)
        return queryset

    def add(self, product, price=None, quantity=1):
        """
        Adds or creates products in cart. For an existing product,
        the quantity is increased and the price is ignored.
        """
        quantity = int(quantity)
        if quantity < 1:
            raise ValueError('Quantity must be at least 1 when adding to cart')
        if product in self.products:
            self._items_dict[product.pk].quantity += quantity
        else:
            if price == None:
                raise ValueError('Missing price when adding to cart')
            self._items_dict[product.pk] = CartItem(product, quantity, price)
        self.update_session()

    @property
    def items(self):
        """
        The list of cart items.
        """
        return self._items_dict.values()

    @property
    def products(self):
        """
        The list of associated products.
        """
        return [item.product for item in self.items]