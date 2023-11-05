quantity = int(input("Number of products purchased: "))
price = int(input("Product price: "))

total = 0

for i in range (1, quantity + 1):
    if i > 2:
        total += price * 0.75
    else:
        total += price

print(f"Amount to pay: {total}")