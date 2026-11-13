import pytest

from inventory import Inventory
from supplier import Supplier
from csv_loader import load_products


@pytest.fixture
def supplier():
    return Supplier(
        "S001",
        "ABC Supplier",
        "abc@example.com"
    )


def test_load_valid_products(tmp_path, supplier, capsys):
    csv_file = tmp_path / "products.csv"

    csv_file.write_text(
        "product_type,product_id,name,price,stock_quantity\n"
        "physical,101,Desk Lamp,25.00,10\n"
        "digital,102,Photo Editor,49.90,100\n",
        encoding="utf-8"
    )

    inventory = Inventory()

    load_products(str(csv_file), inventory, supplier)

    assert len(inventory.products) == 2

    output = capsys.readouterr().out
    assert "Successfully loaded 2 products." in output
    assert "Load attempt finished." in output


def test_missing_csv_file(tmp_path, supplier, capsys):
    csv_file = tmp_path / "missing.csv"
    inventory = Inventory()

    load_products(str(csv_file), inventory, supplier)

    assert len(inventory.products) == 0

    output = capsys.readouterr().out
    assert "File not found:" in output
    assert "Load attempt finished." in output


def test_invalid_rows_are_skipped(tmp_path, supplier, capsys):
    csv_file = tmp_path / "products.csv"

    csv_file.write_text(
        "product_type,product_id,name,price,stock_quantity\n"
        "physical,101,Desk Lamp,25.00,10\n"
        "service,102,Installation,30.00,5\n"
        "physical,103,Office Chair,abc,3\n"
        "digital,104,Photo Editor,49.90,100\n",
        encoding="utf-8"
    )

    inventory = Inventory()

    load_products(str(csv_file), inventory, supplier)

    assert len(inventory.products) == 2

    output = capsys.readouterr().out
    assert "Skipping invalid product row:" in output
    assert "Successfully loaded 2 products." in output
