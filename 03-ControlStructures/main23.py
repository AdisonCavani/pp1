human_years = int(input("Enter the dog's name in human years: "))

result = 0

for i in range(1, human_years + 1):
    if i <=2:
        result += 10.5
    else:
        result += 4

print(f"The dog's age in dog's years is {result} years.")