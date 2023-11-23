from random import randint

number = randint(1, 6)
print(f"Dice rolled: {number}")
print(f"Special number: {number == 1 or number == 6}")