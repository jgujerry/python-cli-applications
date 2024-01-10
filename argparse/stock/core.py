import yfinance as yf


class Stock:
    
    def __init__(self, ticker):
        self.ticker = ticker
    
    def info(self):
        t = yf.Ticker(self.ticker)
        for key, value in t.info.items():
            print("Key:", key, "Value:", value)
