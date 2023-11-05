def different(n1, n2, n3):
    if n1 == n2 or n1 == n3 or n2 == n3:
        return False
    return True

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

diff = "different" if different(first, second, third) else "the same"

print(f"Numbers {first}, {second} and {third} are {diff}")