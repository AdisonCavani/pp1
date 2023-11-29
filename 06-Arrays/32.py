def occurs(number: int, array: list):
  return array.count(number) != 0

arr = [15, 38, 7, 23, 14]
number = 23

print(f"Number: {number}")
print(f"Array: {arr}")

exist = occurs(number, arr)

if exist:
  print(f"Result: number {number} appears in the array")
else:
  print(f"Result: number {number} does not appear in the array")
