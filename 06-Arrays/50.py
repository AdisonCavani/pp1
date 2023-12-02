arr = [[-38, 19], [5,40],[-7,11],[29,16]]

min = 0
min_col = 0
min_row = 0

max = 0
max_col = 0
max_row = 0

for i, array in enumerate(arr):
  for j, num in enumerate(array):
    if num < min or (i == 0 and j == 0):
      min = num
      min_col = i + 1
      min_row = j + 1
    if num > max or (i == 0 and j == 0):
      max = num
      max_col = i + 1
      max_row = j + 1

print(f"Array: {arr}")
print(f"Min: {min}, column: {min_col}, row: {min_row}")
print(f"Max: {max}, column: {max_col}, row: {max_row}")