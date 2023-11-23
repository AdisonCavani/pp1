from random import randint

rand = randint(1, 6)
number = int(input("Guess the number: "))

print(number == rand)