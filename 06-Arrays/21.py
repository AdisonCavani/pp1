arr = [15, 8, 31, 47, 2, 19]

print(f"existed array: {arr}")
print("reverse array: [", end="")

i = len(arr) - 1

while i != -1:
  if i != 0:
    print(f"{arr[i]}, ", end="")
  else:
    print(arr[i], end="")

  i -= 1

print("]")