arr = [[7, 3, 7, 9, 0], [2, 9, 0, 1, 5], [3, 8, 6, 4, 7], [8, 7, 1, 1, 5]]

sum = 0

for i in arr:
  for j, num in enumerate(i):
    if j == len(i) - 1:
      sum += num

print(f"Array: {arr}")
print(f"Sum: {sum}")