# Welcome to our restaurant management system! This system is designed to help you manage your restaurant operations efficiently. You can use it to track orde₹, manage inventory, and handle customer reservations.
# Pizza: ₹40 Pasta: ₹50 Burger: ₹60 Salad: ₹70 Coffee: ₹80
# Enter your fi₹t item you want to order: Pasta
# Order of Pasta has been added to your order. 
# Do you want to order something else? (yes/no): yes
# Enter you next item you want to order: Burger
# your order of coffee has been added to your order.
# The total amount for your order is: ₹110

#define the menu of the restaurant
menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80,

}
#Greet

print("="*50)
print("      🍕 WELCOME TO RAJ RESTAURANT 🍔")
print("="*50)
print("           MENU CARD")
print("-"*50)
print("Pizza   : ₹40")
print("Pasta   : ₹50")
print("Burger  : ₹60")
print("Salad   : ₹70")
print("Coffee  : ₹80")
print("-"*50)

order_total = 0
item_1 = input("Enter item: ").title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Ordered item{item_1} is not available yet ! ")
another_order = input("Do you want to add another item? (yes/No)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")
    print(f"The total amount of items to pay is {order_total}")