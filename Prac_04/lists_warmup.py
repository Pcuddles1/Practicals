
numbers = [3, 1, 4, 1, 5, 9, 2]
# 3
# 2
# 1
# 3, 1, 4, 1, 5, 9
# 1
# True
# False
# False
# 3, 1, 4, 1, 5, 9, 2, 6, 5, 3

numbers.insert(0, "ten")
numbers.insert(8, 1)
print(numbers)
print(numbers[2:8])

for number in numbers:
    if number == 9:
        print("contains 9")