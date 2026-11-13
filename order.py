from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy = None):
        if not isinstance(order_id, str) or not order_id.strip():
            raise ValueError("Order ID cannot be empty.")

        self._order_id: str = order_id
        self._order_lines: list[OrderLine] = []
        self._discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    @property
    def order_id(self) -> str:
        return self._order_id

    @property
    def order_lines(self) -> list[OrderLine]:
        return self._order_lines.copy()

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self._order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0

        for line in self._order_lines:
            total += line.calculate_subtotal()

        return self._discount.apply(total)

    def set_discount(self, discount: DiscountStrategy):
        if not isinstance(discount, DiscountStrategy):
            raise TypeError("Invalid discount strategy.")

        self._discount = discount