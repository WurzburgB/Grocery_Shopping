class Store:
    # Store Items
    def __init__(self, name, price, quantity, code):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.code = code

    def __repr__(self):
        return f"{self.name}, we have {self.quantity} in stock. Each unit cost ${self.price} and the item code is: {self.code}"


class Shopper:
    # Shopper attributes. Shopper must have "name", "budget", "wallet amount", "cart"
    def __init__(self, name, budget, shopping_cart):
        self.name = name
        self.budget = budget
        self.shopping_cart = shopping_cart

    def __repr__(self):
        # Printing a shopper will tell you their name, their current shopping budget
        return f"Hi, my name is {self.name}. I'm here to shop for a few items my current budget is ${self.budget}."


# Store Items
a = Store("Bananas", 3, 9, "a")
b = Store("Apples", 4, 12, "b")
c = Store("Lettuce", 2, 10, "c")
d = Store("Water", 6, 30, "d")
e = Store("Chicken", 15, 20, "e")
f = Store("Ground Beef", 10, 14, "f")
g = Store("Steak", 25, 9, "g")
h = Store("Eggs", 8, 25, "h")
i = Store("Apple Juice", 6, 3, "i")
j = Store("Rice", 8, 24, "j")
k = Store("All Purpose Flour", 7, 7, "k")
l = Store("Potatoes", 4, 13, "l")
m = Store("Onions", 3, 6, "m")
n = Store("Candy Bar", 1, 30, "n")
o = Store("Frozen Pizza", 7, 3, "o")
p = Store("Blueberries", 5, 21, "p")
q = Store("Bread", 4, 25, "q")
r = Store("Milk", 3, 8, "r")
s = Store("Butter", 4, 16, "s")
t = Store("Cheese", 5, 10, "t")

# List of item instances
store_items = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]

# Welcome message
userName = input("Hi, what would you like to be called? ")
welcome = float(input(f"""
Welcome to Publix {userName}!
If you don't mind me asking, what is your budget for the day? 
Please enter a whole number: """))

start = input(f"Would you like to get started with your shopping? """)

shopper_one_cart = []
# Current Shopper
shopper_one = Shopper(userName, welcome, shopper_one_cart)

# Introduce menu
if start == 'yes' or 'Yes':
    print("******MENU******")
    for item in store_items:
        print(f"{item.name}: ${item.price}, item code: {item.code} ")
else:
    print("Okay take a look around!")

inventory_message = input(
    "\nAbove is our list of instock items which item would you like to add to your cart first? Type the item code: ")
print("Above is our list of instock items which item would you like to add to your cart first?")

add_item = input("Choose item: ")
print(add_item)

# if add_item in store_items:


# Add item to cart
if inventory_message == 'a':
    shopper_one_cart.append(a.name)
elif inventory_message == 'b':
    shopper_one_cart.append(b.name)
elif inventory_message == 'c':
    shopper_one_cart.append(c.name)
elif inventory_message == 'd':
    shopper_one_cart.append(d.name)
elif inventory_message == 'e':
    shopper_one_cart.append(e.name)

# print(shopper_one.shopping_cart)

want_more = input("Would like to add another item? Enter yes or no: ")

if want_more == "yes":
    print(add_item)

if want_more == "no":
    print("here is you total: ")