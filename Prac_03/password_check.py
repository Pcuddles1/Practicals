


def main():
    finished = False
    min_length = 2

    while not finished:
        password = get_password()
        finished = print_asterisks(finished, min_length, password)


def print_asterisks(finished, min_length, password):
    if len(password) >= min_length:
        for i in range(0, len(password), 1):
            print("*", end='')
            finished = True
    else:
        print("Password invalid")
    return finished


def get_password():
    password = input("enter password: ")
    return password


main()