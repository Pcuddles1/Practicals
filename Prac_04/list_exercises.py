

def main():
    #numbers = inputs()
    #display_questions(numbers)
    part_2()


def inputs():
    numbers = []
    for i in range(0, 5, 1):
        user_number = int(input("number: "))
        numbers.append(user_number)
    print(numbers)
    return numbers

def display_questions(numbers):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    numbers.sort()
    print(numbers)
    print("The smallest number is {}".format(numbers[0]))
    print("The largest number is {}".format(numbers[-1]))
    num = (sum(numbers))/len(numbers)
    print("The average of the numbers is {}".format(num))

def part_2():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Please enter username: ")
    passs = 0
    for i in range(len(usernames)):
        if username == usernames[i]:
            passs = 1
    if passs == 1:
        print("Access granted")
    else:
        print("Access denied")

main()
