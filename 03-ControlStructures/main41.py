pin = "0805"

for i in range(1, 4):
  guess = input("Enter the PIN code: ")

  if guess == pin:
    break

  print("Incorrect...")

if guess == pin:
  print("Access granted.")
else:
  print("Sorry, your payment card has been blocked.")