import itertools

class Order:
    id_obj = itertools.count()

    def __init__(self, order_type: str, price: float, quantity: int) -> None:
        self.id = next(self.id_obj)
        self.order_type = order_type
        self.price = price
        self.quantity = quantity

    def __eq__(self, other: object) -> bool:
        return self.price == other.price and self.order_type == other.order_type and self.quantity == other.quantity and self.id == other.id