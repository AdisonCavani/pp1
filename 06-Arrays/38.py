arr = [7, 12, 8, 1, 0, 43, 4]

print(f"Array: {arr}")

num = int(input("Enter number: "))

new_arr = []

for item in arr:
  if num < item:
    new_arr.append(item)

print(f"New array: {new_arr}")