import csv
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory

def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:

    loaded_count = 0

    try:
        with open(path, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    product_type = row["product_type"].strip().lower()

                    product = ProductFactory.create(
                        product_type,
                        int(row["product_id"]),
                        row["name"],
                        float(row["price"]),
                        int(row["stock_quantity"]),
                        supplier,
                        weight=1.0 if product_type == "physical" else None,
                        download_size=1.0 if product_type == "digital" else None
                    )

                    inventory.add_product(product)
                    loaded_count += 1

                except (ValueError, TypeError, KeyError) as error:
                    print(f"Skipping invalid product row: {error}")

    except FileNotFoundError:
        print(f"File not found: {path}")

    except OSError as error:
        print(f"Could not read file: {error}")

    else:
        print(f"Successfully loaded {loaded_count} products.")

    finally:
        print("Load attempt finished.")