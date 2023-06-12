# Task 1.
# Create a class Product with properties name, price, and quantity.
# Create a child class Book that inherits from Product and adds a property author and a method called read.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"Book: {self.name} by {self.author}.")


book = Book("The Great Gatsby", 9.99, 10, "F. Scott Fitzgerald")
print(f"Book: {book.name}")
print(f"Price: {book.price}")
print(f"Quantity: {book.quantity}")
print(f"Author: {book.author}")

book.read()


# Task 2.
# Create a class Restaurant with properties name, cuisine, and menu.
class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


# Create a child class FastFood that inherits from Restaurant and adds a property drive_thru (a boolean indicating whether the restaurant has a drive-thru or not)
class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    # and a method called order which takes in the dish name and quantity and returns the total cost of the order.
    # The method should also update the menu dictionary to subtract the ordered quantity from the available quantity.
    # If the dish is not available or if the requested quantity is greater than the available quantity, the method should return a message
    # indicating that the order cannot be fulfilled.
    def order(self, dish_name, quantity):
        if dish_name in self.menu:
            dish = self.menu[dish_name]
            if quantity <= dish['quantity']:
                total_cost = dish['price'] * quantity
                dish['quantity'] -= quantity
                return total_cost
            else:
                return "Requested quantity not available"
        else:
            return "Dish not available"


# The menu property should be a dictionary with keys being the dish name and values being the price.
menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # 25
print(mc.order('burger', 15))  # Requested quantity not available
print(mc.order('soup', 5))  # Dish not available
