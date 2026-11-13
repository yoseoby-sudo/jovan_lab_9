from inventory import Inventory
from supplier import Supplier
from csv_loader import load_products

# Create an empty inventory
inventory = Inventory()

# Create a supplier for the imported products
supplier = Supplier(
    "S001",
    "ABC Supplier",
    "abc@example.com"
)

# Load products from CSV
load_products("products.csv", inventory, supplier)

# Display imported products
print("\nImported Products:")
inventory.display_all()

print("\nTotal products:", len(inventory.products))