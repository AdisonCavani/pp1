arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

print(f"Array: {arr}")

for i, array in enumerate(arr):
  temp = array[0]
  array[0] = array[2]
  array[2] = temp

print(f"After: {arr}")