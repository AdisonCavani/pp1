file = open("countries.txt", "r")

for i, line in enumerate(file):
    print(f"{i + 1}. {line}", end="")

file.close()
print()