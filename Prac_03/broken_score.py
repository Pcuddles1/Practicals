"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

global score_print



def check_score(score):
    if score < 0:
        score_print = 1
    elif score > 100:
        score_print = 1
    elif score >= 90:
        score_print = 2
    elif score >= 50:
        score_print = 3
    else:
        score_print = 4
#    print(score_print)
    return score_print


def main():
    score = float(input("Enter score: "))
    check_score(score, score_print)
    print(score_print)
    if score_print == 1:
        print("Invalid score")
    elif score_print == 2:
        print("Excellent")
    elif score_print == 3:
        print("Passable")
    elif score_print == 4:
        print("bad")

main()