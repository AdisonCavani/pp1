from random import randint

with open("22.txt", "a") as file:
  for i in range(1, 51):
    file.write(f"{randint(100, 999)}\n")