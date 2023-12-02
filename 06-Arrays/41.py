arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 4, 3, 5, 6, 10]

condition = True

for num in arr1:
  if arr2.count(num) == 0:
    condition = False

print(condition)
