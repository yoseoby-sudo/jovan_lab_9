import pytest

from order import Order
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount
from physical_product import PhysicalProduct
from supplier import Supplier


def test_no_discount():
    strategy = NoDiscount()
    assert strategy.apply(250) == 250


def test_percentage_discount():
    strategy = PercentageDiscount(10)
    assert strategy.apply(250) == 225


def test_bulk_discount_applied():
    strategy = BulkDiscount(200, 20)
    assert strategy.apply(250) == 230


def test_bulk_discount_not_applied():
    strategy = BulkDiscount(200, 20)
    assert strategy.apply(150) == 150


def test_student_discount():
    strategy = StudentDiscount()
    assert strategy.apply(250) == 237.5


def test_change_discount_strategy():
    supplier = Supplier(
        "S001",
        "ABC Supplier",
        "abc@example.com"
    )

    product = PhysicalProduct(
        101,
        "Desk Lamp",
        250,
        10,
        1.5,
        supplier
    )

    order = Order("ORD001")
    order.add_order_line(product, 2)

    # Original total: 500
    assert order.calculate_total() == 500

    # Bulk discount: 500 - 20 = 480
    order.set_discount(BulkDiscount(200, 20))
    assert order.calculate_total() == 480

    # Percentage discount: 500 - 10% = 450
    order.set_discount(PercentageDiscount(10))
    assert order.calculate_total() == 450


def test_invalid_percentage():
    with pytest.raises(ValueError):
        PercentageDiscount(120)


def test_invalid_discount_strategy():
    order = Order("ORD001")

    with pytest.raises(TypeError):
        order.set_discount("10%")
