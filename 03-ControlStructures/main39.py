a = 4
b = 15

for i in range(1, b + 1):
  print("*", end="")

print()

for i in range(1, a - 1):
  for j in range(1, b + 1):
    if j == 1 or j == b:
      print("*", end="")
    else:
      print(" ", end="")

  print()

for i in range(1, b + 1):
  print("*", end="")
