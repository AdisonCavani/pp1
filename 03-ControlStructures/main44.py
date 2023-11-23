quantity = 0
sum = 0
mean = 0

while True:
  number = int(input("Enter number: "))

  if number == 0:
    break

  quantity += 1
  sum += number
  mean = sum / quantity

print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={round(mean)}")