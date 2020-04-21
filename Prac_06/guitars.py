
from Prac_06.guitar import Guitar

"""
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
"""

guitars = []

print("My guitars!")
name = input("Name: ")

while name != "":
    year = input("Year: ")
    cost = input("Cost: $")
    guitars.append(Guitar(name, year, cost))
    name = input("Name: ")


