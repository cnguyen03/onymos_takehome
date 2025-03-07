import threading
import time
import random

from order_book import OrderBook

order_book = OrderBook()

def simulate_orders():
    tickers = [f"TICKER {i}" for i in range(1, 1025)] # Tickers 1-1024
    while True:
        order_type = "Buy" if random.randint(0, 1) else "Sell"
        ticker = random.choice(tickers)
        quantity = random.randint(1, 100)
        price = round(random.uniform(10, 500), 2)
        order_book.add_order(order_type, ticker, quantity, price)
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == '__main__':
    # Start the order simulation in multiple threads
    threads = [threading.Thread(target=simulate_orders) for _ in range(5)]
    for thread in threads:
        thread.start()