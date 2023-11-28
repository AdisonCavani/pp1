arr = [34, 7, 19, 4, 21, 8]

counter = len(arr) - 1
sum = 0

while counter != -1:
  if arr[counter] % 2 == 0:
    sum += arr[counter]

  counter -= 1

print(f"Sum of even numbers in array: {sum}")