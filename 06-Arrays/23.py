arr = [-15, 8, -31, 47, -2, 19]

max = 0
min = 0

for i, item in enumerate(arr):
  if item > max or i == 0:
    max = item
  if item < min or i == 0:
    min = item

print(f"Max: {max}")
print(f"Min: {min}")