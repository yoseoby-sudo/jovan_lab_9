
import pytest

from product_factory import ProductFactory
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


@pytest.fixture
def supplier():
    return Supplier(
        "S001",
        "ABC Supplier",
        "abc@example.com"
    )


def test_create_physical_product(supplier):
    product = ProductFactory.create(
        "physical",
        101,
        "Desk Lamp",
        25.00,
        10,
        supplier,
        weight=1.5
    )

    assert isinstance(product, PhysicalProduct)
    assert product.name == "Desk Lamp"
    assert product.price == 25.00


def test_create_digital_product(supplier):
    product = ProductFactory.create(
        "digital",
        102,
        "Photo Editor",
        49.90,
        100,
        supplier,
        download_size=500
    )

    assert isinstance(product, DigitalProduct)
    assert product.name == "Photo Editor"
    assert product.price == 49.90


def test_unknown_product_type(supplier):
    with pytest.raises(ValueError):
        ProductFactory.create(
            "service",
            103,
            "Installation",
            30.00,
            5,
            supplier
        )
