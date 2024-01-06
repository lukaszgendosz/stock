from order import Order
    
class Stock:
    def __init__(self) -> None:
        self.orders = []

    def add_order(self, new_order: Order) -> None:
        self.orders.append(new_order)
    
    def remove_order(self, new_order: Order) -> None:
        orders = self.get_orders_by_price_and_type(new_order.order_type, new_order.price)

        for order in orders:
            if order.quantity >= new_order.quantity:
                order.quantity -= new_order.quantity
                break
            else:
                new_order.quantity -= order.quantinty
                order.quantinty = 0
                continue
        self.remove_empty_orders()
    
    def display_sum_of_best_orders(self) -> None:
        buy_message = self.get_best_orders_info("Buy")
        sell_message = self.get_best_orders_info("Sell")
        final_message = f'{buy_message}\n{sell_message}\n'
        print(final_message)

    def get_best_orders_info(self, order_type: str, ) -> None:
        orders = [order for order in self.orders if order.order_type == order_type]
        if orders:
            if order_type == "Buy":
                best_order_price = max([buy_order.price for buy_order in orders])
            if order_type == "Sell":
                best_order_price = min([buy_order.price for buy_order in orders])
            matching_best_orders = self.get_orders_by_price_and_type(order_type, best_order_price)
            best_order_quantity = sum([matching_buy_order.quantity for matching_buy_order in matching_best_orders])
            message = f"The best {order_type.lower()} order price is {best_order_price} with a quantity of {best_order_quantity} actions."
        else:
            message = f"No {order_type.lower()} orders yet!"
        
        return message


    def get_orders_by_price_and_type(self, order_type: str, price: float) -> list:
        matching_orders = [order for order in self.orders if order.price == price and order.order_type == order_type]
        return matching_orders
    
    def remove_empty_orders(self) -> None:
        empty_order_indexes = [self.orders.index(order) for order in self.orders if order.quantity == 0]
        if empty_order_indexes:
            empty_order_indexes.sort(reverse=True)
            for index in empty_order_indexes:
                self.orders.pop(index)


