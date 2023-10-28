registration = input("Enter vehicle registration number: ")

car_from_cracow = registration.startswith("KR") or registration.startswith("KK")

print("Car from Cracow: ", car_from_cracow)
