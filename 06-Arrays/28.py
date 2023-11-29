def compare(array1: list, array2: list):
  if len(array1) != len(array2):
    return False
  
  for i, item in enumerate(array1):
    if item != array2[i]:
      return False
  
  return True

print(f"a. {compare(["water", "book", "sky"], ["water", "book", "sky"])}")
print(f"b. {compare([True, False], [True, False, True])}")
print(f"c. {compare([5, 3, 1], [5, 3, 1])}")
print(f"d. {compare([3, 2, 1], [3, 2])}")