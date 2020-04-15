
name_file = open("name.txt", 'w')
name = str(input("enter your name: "))
print(name, file = name_file)
name_file.close()

name_file = open("name.txt", 'r')
show_name = name_file.read()
print(show_name)

number_file = open("numbers.txt", 'r')
first_number = int(number_file.readline())
second_number = int(number_file.readline(4-5))
show_calculation = first_number + second_number
print(show_calculation, "\n")



number_file = open("numbers.txt", 'r')
total_numbers = number_file.readline()
for line in number_file:
    total_numbers = total_numbers + line
print(total_numbers)
