import sys
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

    #Calculate subtotal
    def subtotal(self, shopping_cart, list_of_items):
        total = 0

        for item in shopping_cart:
            for product in list_of_items:
                if item == product.code:
                    total += product.price
        return total
    #Calculate Tax
    def tax(self, shopping_cart, list_of_items):
        subtotal = self.subtotal(shopping_cart, list_of_items)
        tax_rate = 0.08
        tax_amount = subtotal * tax_rate
        return tax_amount

    #Totaling price of items plus tax
    def total_cart(self, shopping_cart, list_of_items):
        total = 0
        tax = self.tax(shopping_cart, list_of_items)
        for item_code in shopping_cart:
            for product in list_of_items:
                if item_code == product.code:
                    total += product.price
                    break  # Stop searching for the item once found
        return total + tax

    #Cart itemization
    def receipt(self, shopping_cart, list_of_items):
        itemization = ''
        item_counts = {}
        for item_code in shopping_cart:
            for product in list_of_items:
                if item_code == product.code:
                    if item_code not in item_counts:
                        item_counts[item_code] = 1
                    else:
                        item_counts[item_code] += 1

        for item_code, quantity in item_counts.items():
            for product in list_of_items:
                if item_code == product.code:
                    itemization += f"{product.name}  ${product.price}  Qty. {quantity}\n"

        return itemization


# Store Items
a = Store("Bananas", 3, 9, "1")
b = Store("Apples", 4, 12, "2")
c = Store("Lettuce", 2, 10, "3")
d = Store("Water", 6, 30, "4")
e = Store("Chicken", 15, 20, "5")
f = Store("Ground Beef", 10, 14, "6")
g = Store("Steak", 25, 9, "7")
h = Store("Eggs", 8, 25, "8")
i = Store("Apple Juice", 6, 3, "9")
j = Store("Rice", 8, 24, "10")
k = Store("All Purpose Flour", 7, 7, "11")
l = Store("Potatoes", 4, 13, "12")
m = Store("Onions", 3, 6, "13")
n = Store("Candy Bar", 1, 30, "14")
o = Store("Frozen Pizza", 7, 3, "15")
p = Store("Blueberries", 5, 21, "16")
q = Store("Bread", 4, 25, "17")
r = Store("Milk", 3, 8, "18")
s = Store("Butter", 4, 16, "19")
t = Store("Cheese", 5, 10, "20")

# List of item instances
store_items = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]

#Test
test_cart = [a, b, c]
test_shopper = Shopper('Wurz', 50, test_cart)




# Welcome message
userName = input("Hi, what would you like to be called? ")
welcome = (f"Welcome to Publix {userName}!")
print(welcome)
start = input(f"Would you like to get started with your shopping? Enter Yes or No: ")



shopper_one_cart = []
# Current Shopper
shopper_one = Shopper(userName, welcome, shopper_one_cart)

# Introduce menu
if start.lower() == 'yes':
    print("*********MENU*********")
    for item in store_items:
        print(f"{item.name}: ${item.price}, item code: {item.code} ")
else:
    print("Okay take a look around!")
    sys.exit()

#Adding items to cart
inventory_message = "\nAbove is our list of stock items which item would you like to add to your cart first?"
print(inventory_message)
while True:
    add_item = input("Enter item code: ")
    print('If you are finished type "Done"\n')
    if add_item.lower() != "done":
        shopper_one_cart.append(add_item)
    elif add_item.lower() == "done":
        break
    else:
        print("Error invalid entry!")
    add_item = float(add_item)



    print(f"Cart Subtotal: ${shopper_one.subtotal(shopper_one_cart, store_items)}")






#Add Tax to receipt
# print(shopper_one.shopping_cart)
print("\n********Receipt********\n")
print(shopper_one.receipt(shopper_one_cart, store_items))
print("********************")
print(f"Subtotal: ${shopper_one.subtotal(shopper_one_cart, store_items)}")
print(f"Tax: ${shopper_one.tax(shopper_one_cart, store_items)}")
print(f"Total: ${shopper_one.total_cart(shopper_one_cart, store_items)}\n")
print("Thank you for shopping with us!")
