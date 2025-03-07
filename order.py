class Order:
    def __init__(self, order_type: str, ticker: str, quantity: int, price: float):
        self.order_type = order_type  # "Buy" or "Sell"
        self.ticker = ticker # Ticker of stock
        self.quantity = quantity # Number of shares
        self.price = price # Price of individual share
        self.next = None