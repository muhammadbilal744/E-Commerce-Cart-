"""
cli.py - Command Line Interface for the E-Commerce Cart System
"""

from src.models import Product, ShoppingCart, NoDiscount, PercentageDiscount


def display_menu():
    print("\n===== E-Commerce Cart Menu =====")
    print("1. Add Product to Cart")
    print("2. Remove Product from Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")


def main():

    # Sample product catalog
    catalog = {
        "LAP123": Product("LAP123", "Laptop", 1000.0),
        "MOU456": Product("MOU456", "Mouse", 50.0),
        "KEY789": Product("KEY789", "Keyboard", 80.0)
    }

    print("Choose Pricing Strategy")
    print("1. No Discount")
    print("2. 10% Discount")

    strategy_choice = input("Enter choice: ")

    if strategy_choice == "2":
        strategy = PercentageDiscount(10)
    else:
        strategy = NoDiscount()

    cart = ShoppingCart(strategy)

    while True:

        display_menu()
        choice = input("Enter option: ")

        # Add product
        if choice == "1":

            sku = input("Enter product SKU: ")

            if sku not in catalog:
                print("Product not found.")
                continue

            try:
                qty = int(input("Enter quantity: "))
                cart.add(catalog[sku], qty)
                print("Product added to cart.")
            except ValueError as e:
                print("Error:", e)

        # Remove product
        elif choice == "2":

            sku = input("Enter product SKU to remove: ")

            try:
                cart.remove(sku)
                print("Product removed.")
            except KeyError:
                print("Product not found in cart.")

        # View cart
        elif choice == "3":

            items = cart.items()

            if not items:
                print("Cart is empty.")
                continue

            print("\nItems in Cart:")
            for item in items:
                print(f"{item.product.name} | Qty: {item.qty} | Subtotal: ${item.subtotal()}")

            print("Cart Subtotal:", cart.subtotal())

        # Checkout
        elif choice == "4":

            items = cart.get_items()

            if not items:
                print("Cart is empty.")
                continue

            print("\n===== Receipt =====")

            for item in items:
                print(f"{item.product.name} x {item.qty} = ${item.subtotal()}")

            print("-----------------------")
            print("Subtotal:", cart.subtotal())
            print("Total after discount:", cart.total())

        # Exit
        elif choice == "5":
            print("Thank you for shopping!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()