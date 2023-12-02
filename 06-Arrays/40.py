arr = [1, 23, 5, 382, 1, 17, 4, 906]

string = ""

for num in arr:
  string += f"|{num}"

string += "|"

print("-" * len(string))
print(string)
print("-" * len(string))