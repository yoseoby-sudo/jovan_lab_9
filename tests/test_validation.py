import pytest

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from order_line import OrderLine


@pytest.fixture
def supplier():
    return Supplier(
        "S001",
        "ABC Supplier",
        "abc@example.com"
    )


def test_product_rejects_zero_price(supplier):
    with pytest.raises(ValueError):
        PhysicalProduct(
            101, "Desk Lamp", 0, 10, 1.5, supplier
        )


def test_product_rejects_negative_price(supplier):
    with pytest.raises(ValueError):
        DigitalProduct(
            102, "Photo Editor", -10, 100, 500, supplier
        )


def test_product_rejects_negative_stock(supplier):
    with pytest.raises(ValueError):
        PhysicalProduct(
            103, "Office Chair", 50, -1, 5, supplier
        )


def test_product_accepts_zero_stock(supplier):
    product = PhysicalProduct(
        104, "Monitor", 100, 0, 3, supplier
    )

    assert product.stock == 0


def test_order_line_rejects_zero_quantity(supplier):
    product = PhysicalProduct(
        105, "Keyboard", 30, 10, 1, supplier
    )

    with pytest.raises(ValueError):
        OrderLine(product, 0)


def test_order_line_rejects_negative_quantity(supplier):
    product = PhysicalProduct(
        106, "Mouse", 20, 10, 1, supplier
    )

    with pytest.raises(ValueError):
        OrderLine(product, -2)
