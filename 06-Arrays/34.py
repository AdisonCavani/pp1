variable = (10, 20, 30, 40, 50)

print(f"Tuple: {variable}")
print("Reverse order: (", end="")

for i in range(len(variable) - 1, -1, -1):
  print(f" {variable[i]}", end=" ")

print(" )")