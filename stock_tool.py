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
    
    def check_stock(self, item):
        """Check how many of one product are in stock.

        Args:
            item: The product name, like rain jacket.
        """
        product_id = self.find_product_id(item)
        if product_id is None:
            return "That product was not found."
        quantity = self.find_quantity(product_id)
        return f"We have {quantity} of the {product_id} in stock."