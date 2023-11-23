price = float(input("Enter price: "))
discount = int(input("Enter discount: "))

final = price - price * (discount / 100)

print(f"Price with discount: {round(final, 2)}")
print(f"Reduction: {round(price - final, 2)}")