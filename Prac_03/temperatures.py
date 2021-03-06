
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

def main():
    def celsius_to_fahrenheit():
        global fahrenheit
        fahrenheit = celsius * 9.0 / 5 + 32


    def fahrenheit_to_celsius():
        global celsius
        celsius = (fahrenheit - 32) * 5 / 9.0


    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            celsius_to_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            fahrenheit_to_celsius()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()