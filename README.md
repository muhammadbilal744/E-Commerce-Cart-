# E-Commerce Cart System (Python OOP Project)

A simple **E-Commerce Cart System** built using **Python and Object-Oriented Programming (OOP)** concepts. 
This project simulates basic shopping cart operations such as browsing a product catalog, adding or removing items, calculating totals, and applying dynamic discount codes using the Strategy Design Pattern.

### Features

* View product catalog
* Add items to cart (auto-updates quantity for duplicates)
* Remove items from cart completely
* Apply dynamic discount codes (10% off, 20% off, etc.)
* Calculate subtotals, discount amounts, and final totals
* Generate detailed cart receipts
* Unit testing using Python `unittest`
* Interactive Command Line Interface (CLI)

### Concepts Used

This project demonstrates the following OOP and design concepts:
* Classes and Objects
* Strategy Design Pattern (Open/Closed Principle)
* Encapsulation
* Composition
* Inheritance & Polymorphism
* Abstract Classes (ABC)
* Dataclasses
* Exception Handling
* Unit Testing

### Project Structure

```text
oop-ecommerce-cart
│
├── src
│   ├── __init__.py
│   └── models.py            # Core cart and pricing strategy logic
│
├── tests
│   ├── __init__.py
│   └── test_cart.py         # Unit tests
│
├── cli.py                   # Command Line Interface
└── README.md


How to Run the Program
Open the terminal in the project folder.

Run the CLI application:

Bash
python cli.py
You will see the shopping cart menu:

Plaintext
1. View Product Catalog
2. Add Item to Cart
3. Remove Item from Cart
4. Apply Discount Code
5. View Cart & Checkout
6. Exit
Running Unit Tests
Run the tests using:

Bash
python -m unittest tests/test_cart.py
If everything works correctly, you will see:

Plaintext
...........
----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
