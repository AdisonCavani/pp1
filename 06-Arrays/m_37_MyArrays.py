def second_largest(array: list):
  array.sort()

  return array[len(array) - 2]

def diff_min_max(array: list):
  min = 0
  max = 0

  for i, item in enumerate(array):
    if item < min or i == 0:
      min = item
    if item > max or i == 0:
      max = item

  return max - min

def median(array: list):
  array.sort()

  return array[len(array) // 2]

def min_max(array: list):
  min = 0
  max = 0

  for i, item in enumerate(array):
    if item < min or i == 0:
      min = item
    if item > max or i == 0:
      max = item

  return [min, max]

def array_str(array: list):
  string = ""

  for i, item in enumerate(array):
    if i != len(array) - 1:
      string += f"{item}-"
    else:
      string += str(item)

  return string