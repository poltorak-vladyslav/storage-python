class Product:
    def __init__(self, product_id):
        self.product_id = product_id

    def __repr__(self):
        return f"Продукт {self.product_id}"