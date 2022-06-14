from domain.core import (
    BaseRepository,
    Singleton,
)
from domain.orders.models import (
    Bouquet,
    Order,
    OrderDetails,
    Payment,
)


class BouquetRepository(BaseRepository, metaclass=type(Singleton)):
    BASE_CLASS = Bouquet


class OrderRepository(BaseRepository, metaclass=type(Singleton)):
    BASE_CLASS = Order


class OrderDetailsRepository(BaseRepository, metaclass=type(Singleton)):
    BASE_CLASS = OrderDetails


class PaymentRepository(BaseRepository, metaclass=type(Singleton)):
    BASE_CLASS = Payment
