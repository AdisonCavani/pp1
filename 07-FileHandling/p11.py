sum = 0
file = open("numbers.txt", "r")

print("Numbers: ", end="")

for num in file:
    num = int(num)
    print(num, end=" ")
    sum += int(num)

print()

print(f"Sum: {sum}")