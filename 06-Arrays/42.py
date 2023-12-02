from random import randint

def rand_elem(array: list):
  return array[randint(0, len(array) - 1)]

arr = [6, 12, 2, 10, 0]

print(f"Array: {arr}")
print(f"Random item: {rand_elem(arr)}")