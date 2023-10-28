from math import sqrt

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

s =  (a + b + c) / 2

area = sqrt(s * (s - a) * (s - b) * (s - c))
circumference = a + b + c

print("Triangle area: ", area)
print("Triangle circumference: ", circumference)