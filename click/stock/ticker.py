import yfinance as yf


def get_stock_info(ticker):
    """Return the stock information for a given ticker"""
    t = yf.Ticker(ticker)
    return t.info
