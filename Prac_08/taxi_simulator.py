from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    finished = False
    chosen = False
    fare = 0
    taxis = [Taxi(100,"Prius"), SilverServiceTaxi(100,"Limo", 2), SilverServiceTaxi(200,"Hummer", 4)]
    chosen_ride = input("Prius, Limo, Hummer\nChoose your ride(p,l,h):")
    while not finished:
        while not chosen:
                if chosen_ride == "p":
                    taxi = taxis[0]
                    distance = int(input("how far will you drive? "))
                    taxi.drive(distance)
                    print(taxi)
                    chosen = True
                elif chosen_ride == "l":
                    taxi = taxis[1]
                    distance = int(input("how far will you drive? "))
                    taxi.drive(distance)
                    print(taxi)
                    chosen = True
                elif chosen_ride == "h":
                    taxi = taxis[2]
                    distance = int(input("how far will you drive? "))
                    taxi.drive(distance)
                    print(taxi)
                    chosen = True
                else:
                    print("invalid ride")
                    chosen_ride = input("Prius, Limo, Hummer\nChoose your ride(p,l,h):")
        fare += taxi.get_fare()
        print("current bill at ${:.2f}".format(fare))

        y_n = input("would you like to drive again (y/n)? ")
        answer = False
        while not answer:
            if y_n == "y":
                chosen_ride = input("Prius, Limo, Hummer\nChoose your ride(p,l,h):")
                chosen = False
                answer = True
            elif y_n == "n":
                finished = True
                answer = True
            else:
                print("invalid answer")
                answer = False
    print("final Bill: ${:.2f}".format(fare))










main()
