from stock import Stock
from order import Order

def main():
    orders = [
        ("Buy", "Add", 20.0, 100),
        ("Sell", "Add", 25.0, 200),
        ("Buy", "Add", 23.0, 50),
        ("Buy", "Add", 23.0, 70),
        ("Buy", "Remove", 23.0, 50),
        ("Sell", "Add", 28.0, 100)
    ]

    stock = Stock()

    for order_type, action, price, quantity in orders:
        order = Order(order_type=order_type,
                      price=price,
                      quantity=quantity)
        
        match action:
            case "Add":
                stock.add_order(order)
            case "Remove":
                stock.remove_order(order)
            case _:
                print("Invalid action!")

        stock.display_sum_of_best_orders()

if __name__ == '__main__':
    main()