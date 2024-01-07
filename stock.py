from order import Order

#Class that stores all order objects.
class Stock:
    def __init__(self) -> None:
        self.orders = []

    #Adds new order object.
    def add_order(self, new_order: Order) -> None:
        self.orders.append(new_order)
    
    #I wasn't certain if the 'Remove' action refers to someone buying/selling shares or canceling their order.
    #I implemented it as if someone is buying/selling shares, so it gathers every order with the same order type and price and deducts the shares quantity from the order/orders.
    #If the current buy/sell order has more shares than the quantity someone wants to buy/sell, it simply subtracts the quantity from the order.
    #If the current buy/sell order has fewer shares than the quantity someone wants to buy/sell, it sets the quantity of the current order to 0 and moves on to another one.
    #It's possible that there are not enough shares in existing buy/sell orders, so the user can only buy the quantity that exists for specified price.
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
    
    #Displays the best price for buy and sell orders along with their quantities.
    def display_sum_of_best_orders(self) -> None:
        buy_message = self.get_best_orders_info("Buy")
        sell_message = self.get_best_orders_info("Sell")
        final_message = f'{buy_message}\n{sell_message}\n'
        print(final_message)

    #Gathers the price and quantity of the best order of the specified type and returns a message containing this information.
    def get_best_orders_info(self, order_type: str) -> None:
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

    #Returns all orders of the specified type and price.
    def get_orders_by_price_and_type(self, order_type: str, price: float) -> list:
        matching_orders = [order for order in self.orders if order.price == price and order.order_type == order_type]
        return matching_orders
    
    #Removes all orders from the stock with a quantity equal to 0.
    def remove_empty_orders(self) -> None:
        empty_order_indexes = [self.orders.index(order) for order in self.orders if order.quantity == 0]
        if empty_order_indexes:
            empty_order_indexes.sort(reverse=True)
            for index in empty_order_indexes:
                self.orders.pop(index)


