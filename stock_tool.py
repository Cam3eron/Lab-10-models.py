# stock_tool.py
# Author: Cameron McGraw

class StockLookup:
    """A tool that knows how many of each product are in stock."""

    def __init__(self, stock):
        """Store the stock in this tool can look up."""
        self.stock = stock

    def find_product_id(self, text):
        """Return the first known product ID mentioned in text, or None."""
        for product in self.stock:
            if product in text:
                return product
        return None

    def find_quantity(self, product):
        """Return how many of one product are in stock, or None if unknown."""
        if product in self.stock:
            return self.stock[product]
        return None