arr = [15, 8, 31, 47, 2, 19]

print(f"Array: {arr}")

count = len(arr)
sum = 0

i = count - 1

while i != -1:
  sum += arr[i]
  i -= 1 

print(f"Mean: {sum / count}")