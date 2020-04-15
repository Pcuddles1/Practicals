"""
Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92
"""

number_of_items = int(input("enter number of items: "))
total_price = 0

for i in range(0, number_of_items, 1):
    current_price = int(input("enter price of item: $"))
    total_price = current_price + total_price

if total_price > 100:
    total_price = total_price * 1.1
print("total price is $", total_price)