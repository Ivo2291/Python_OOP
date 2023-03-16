from shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product_name == product.name:
                return product

    def remove(self, product_name):
        product_to_remove = self.find(product_name)

        if product_to_remove:
            self.products.remove(product_to_remove)

    def __repr__(self):
        output = []
        for product in self.products:
            output.append(f"{product.name}: {product.quantity}")

        return "\n".join(output)
