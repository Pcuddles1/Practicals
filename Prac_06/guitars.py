
from Prac_06.guitar import Guitar

guitars = []

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

"""
print("My guitars!")
name = input("Name: ")

while name != "":
    year = input("Year: ")
    cost = input("Cost: $")
    guitars.append(Guitar(name, year, cost))
    name = input("Name: ")
"""


print("These are my Guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage = "(Vintage)" if guitar.is_vintage() else ""
    print("Guitar {}: {} ({}). worth ${:,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, vintage))




