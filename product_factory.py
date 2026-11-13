
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


class ProductFactory:

    @staticmethod
    def create(
        product_type: str,
        product_id: int,
        name: str,
        price: float,
        stock: int,
        supplier,
        weight: float = None,
        download_size: float = None
    ):

        if product_type == "physical":
            return PhysicalProduct(
                product_id,
                name,
                price,
                stock,
                weight,
                supplier
            )

        elif product_type == "digital":
            return DigitalProduct(
                product_id,
                name,
                price,
                stock,
                download_size,
                supplier
            )

        else:
            raise ValueError("Unknown product type.")
