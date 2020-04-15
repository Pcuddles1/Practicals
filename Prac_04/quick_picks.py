import random


def main():
    num_of_picks = int(input("Number of random picks: "))
    for i in range(num_of_picks):
        randoms = []
        randoms = random.randint(1, 45)
        for x in range(0, 6):
            integer = random.randint(1, 45)
            while integer in randoms:
                integer = random.randint(1, 45)
            randoms.append(integer)
        randoms.sort()
        print(randoms)


main()
