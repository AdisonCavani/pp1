arr = [2, 3, 2, 5, 8, 1, 9, 8]

print(f"Array: {arr}")

unique_arr = []

for item in arr:
  if arr.count(item) == 1:
    unique_arr.append(item)

print(f"Unique elements: {unique_arr}")