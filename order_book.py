import threading
from order import Order

class OrderBook:
    def __init__(self):
        self.buy_head = None # LL of bought stocks in desc order
        self.sell_head = None # LL of sold stocks in asc order
        self.lock = threading.Lock() 

    def add_order(self, order_type: str, ticker: str, quantity: int, price: float):
        new_order = Order(order_type, ticker, quantity, price) # Intialize a new order
        
        with self.lock:
            if order_type == "Buy": # Buy
                if not self.buy_head or self.buy_head.price < price:
                    # First buy or greatest priced buy
                    new_order.next = self.buy_head
                    self.buy_head = new_order
                else:
                    current = self.buy_head
                    while current.next and current.next.price >= price:
                        # Find area in LL to place buy
                        current = current.next
                    new_order.next = current.next
                    current.next = new_order
            else:  # Sell
                if not self.sell_head or self.sell_head.price > price:
                    # First sell or smallest priced sell
                    new_order.next = self.sell_head
                    self.sell_head = new_order
                else:
                    current = self.sell_head
                    while current.next and current.next.price <= price:
                        # Find area in LL to place sell
                        current = current.next
                    new_order.next = current.next
                    current.next = new_order
        
        self.match_order() # Match Buy and Sell orders
    
    def match_order(self):
        with self.lock:
            while self.buy_head and self.sell_head and self.buy_head.price >= self.sell_head.price:
                trade_quantity = min(self.buy_head.quantity, self.sell_head.quantity) # Find quantity to trade
                
                print(f"Matched trade executed: {trade_quantity} shares of {self.buy_head.ticker} at ${self.sell_head.price}")
                
                self.buy_head.quantity -= trade_quantity
                self.sell_head.quantity -= trade_quantity
                
                if self.buy_head.quantity == 0:
                    self.buy_head = self.buy_head.next
                if self.sell_head.quantity == 0:
                    self.sell_head = self.sell_head.next