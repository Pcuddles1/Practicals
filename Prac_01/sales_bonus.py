"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = 1

while sales > float("0"):
    sales = float(input("Enter Sales: $"))
    if sales >= float("1000"):
        sales_with_bonus = sales * 1.15
        print(sales_with_bonus)
    else:
        sales_with_bonus = sales * 1.10
        print(sales_with_bonus)
print("Thank You.")
