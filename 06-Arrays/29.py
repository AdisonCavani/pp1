arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

for item in arr1:
  exist = False

  for item2 in arr2:
    if item == item2:
      exist = True
  
  if exist == False:
    print(f"{item} ", end="")
  