arr = [15, 8, 31, 47, 2, 19]

print(f"Array: {arr}")

count = len(arr)
sum = 0

for item in arr:
  sum += item

print(f"Mean: {sum / count}")