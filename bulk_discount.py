from discount_strategy import DiscountStrategy


class BulkDiscount(DiscountStrategy):

    def __init__(self, threshold: float, amount: float):
        if threshold <= 0:
            raise ValueError("Threshold must be greater than zero.")

        if amount < 0:
            raise ValueError("Discount amount cannot be negative.")

        self.threshold = threshold
        self.amount = amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:
            return total - self.amount

        return total
