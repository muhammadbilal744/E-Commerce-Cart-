# test_cart.py - Automated unit tests for the E-Commerce Cart System

import unittest
from src.models import Product, CartItem, ShoppingCart, NoDiscount, PercentageDiscount


class TestCartSystem(unittest.TestCase):

    def setUp(self):
        # Set up standard products and cart for testing
        self.p1 = Product("LAP123", "Laptop", 1000.0)
        self.p2 = Product("MOU456", "Mouse", 50.0)
        self.no_discount = NoDiscount()
        self.cart = ShoppingCart(self.no_discount)

    # ---------- Product & CartItem Tests ----------

    def test_01_cart_item_subtotal(self):
        # CartItem correctly calculates subtotal
        item = CartItem(self.p1, 2)
        self.assertEqual(item.subtotal(), 2000.0)

    def test_02_negative_price_fails(self):
        # Negative product price should raise ValueError
        with self.assertRaises(ValueError):
            Product("BAD001", "Glitch", -10.0)

    # ---------- Shopping Cart Add/Remove Tests ----------

    def test_03_add_product_to_cart(self):
        # Adding a product to the cart works correctly
        self.cart.add(self.p1, 1)
        self.assertEqual(len(self.cart.get_items()), 1)
        self.assertEqual(self.cart.subtotal(), 1000.0)

    def test_04_add_duplicate_product_updates_qty(self):
        # Adding the same product increases quantity
        self.cart.add(self.p1, 1)
        self.cart.add(self.p1, 2)

        items = self.cart.get_items()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].qty, 3)
        self.assertEqual(self.cart.subtotal(), 3000.0)

    def test_05_add_invalid_quantity_fails(self):
        # Zero or negative quantity should raise ValueError
        with self.assertRaises(ValueError):
            self.cart.add(self.p1, 0)

        with self.assertRaises(ValueError):
            self.cart.add(self.p1, -5)

    def test_06_remove_product_from_cart(self):
        # Removing a product should update cart correctly
        self.cart.add(self.p1, 1)
        self.cart.add(self.p2, 1)

        self.cart.remove("LAP123")

        self.assertEqual(len(self.cart.get_items()), 1)
        self.assertEqual(self.cart.subtotal(), 50.0)

    def test_07_remove_nonexistent_product_fails(self):
        # Removing missing product should raise KeyError
        with self.assertRaises(KeyError):
            self.cart.remove("FAKE999")

    # ---------- Strategy Pattern / Discount Tests ----------

    def test_08_no_discount_total(self):
        # Total should equal subtotal when no discount is applied
        self.cart.add(self.p1, 1)
        self.cart.add(self.p2, 2)

        self.assertEqual(self.cart.total(), 1100.0)

    def test_09_percentage_discount_total(self):
        # Percentage discount should reduce total correctly
        discount_strategy = PercentageDiscount(20.0)
        cart_with_discount = ShoppingCart(discount_strategy)

        cart_with_discount.add(self.p1, 1)
        cart_with_discount.add(self.p2, 2)

        self.assertEqual(cart_with_discount.total(), 880.0)

    def test_10_invalid_percentage_fails(self):
        # Invalid discount percentage should raise ValueError
        with self.assertRaises(ValueError):
            PercentageDiscount(-10.0)

        with self.assertRaises(ValueError):
            PercentageDiscount(150.0)


if __name__ == "__main__":
    unittest.main()
    
    
# to run this file ( python -m unittest tests/test_cart.py)
