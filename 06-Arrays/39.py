arr = [7, 12, 8, 1, 0, 43, 4]

print(f"Array: {arr}")

arr_odd = []
arr_even = []

for num in arr:
  if num % 2 == 0:
    arr_even.append(num)
  else:
    arr_odd.append(num)

new_arr = arr_even + arr_odd

print(f"New array: {new_arr}")