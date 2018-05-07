from random import *
money = int(input("How much money would you like to start with? "))
print("You have " + str(money) + " dollars.")
while money > 0:
    lastin = input("How much Money would you like to bet? ")
    if int(lastin) <= money:
        int(money) - int(lastin)
        rand = randint(1,2)
        if int(rand) == 1:
            money +=(int(lastin) * .5)
            print("You Win! Your current funds are: " + str(money))
        else:
            money -= int(lastin)
            print("You lose! Your current funds are: " + str(money))
    else:
        print("You do not have enough money!")
print("You are a loser!")
