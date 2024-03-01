# server3.py

import random

def getQuotes():
    """Returns mock stock data."""
    # Mock data for two stocks: Stock A and Stock B
    stock_A = {
        'stock': 'Stock A',
        'top_bid': {'price': random.randint(100, 200)},
        'top_ask': {'price': random.randint(100, 200)}
    }
    stock_B = {
        'stock': 'Stock B',
        'top_bid': {'price': random.randint(100, 200)},
        'top_ask': {'price': random.randint(100, 200)}
    }
    return [stock_A, stock_B]
