with open("23.txt", "a") as file:
  for i in range(1, 11):
    file.write(f"{i},{pow(i, 2)},{pow(i, 3)}\n")