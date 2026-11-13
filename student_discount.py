from discount_strategy import DiscountStrategy


class StudentDiscount(DiscountStrategy):

    def apply(self, total: float) -> float:
        discount = total * 0.05
        return total - discount
