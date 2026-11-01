# order_tool.py
# Author: Cameron McGraw


class OrderLookup:
    """A tool that knows about orders. It knows nothing about chatting."""

    def __init__(self, orders):
        """Store the orders in this tool can look up."""
        self.orders = orders

    def find_order_id(self, text):
        """Return the first known order ID mentioned in text, or None."""
        for order_id in self.orders:
            if order_id in text:
                return order_id
        return None

    def find_status(self, order_id):
        """Return the status of one ordeeer, or None if there is no such order."""
        if order_id in self.orders:
            return self.orders[order_id]
        return None