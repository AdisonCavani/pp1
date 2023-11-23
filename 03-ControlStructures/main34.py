amount = int(input("Enter the amount in PLN: "))

print(f"The amount of PLN {amount} in coins:")

five = 0
two = 0
one = 0

while amount >= 5:
  amount -= 5
  five += 1

while amount >= 2:
  amount -= 2
  two += 1

while amount >= 1:
  amount -= 1
  one += 1

print(f"5 zł - {five}")
print(f"2 zł - {two}")
print(f"1 zł - {one}")