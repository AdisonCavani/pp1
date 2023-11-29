def bubblesort(array: list):
  for i, _ in enumerate(array):
    for j, _ in enumerate(array):
      if arr[j] > arr[i]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

arr = [6, 5, 4, 3, 2, 1, 0]

print(f"Before: {arr}")

bubblesort(arr)

print(f"After: {arr}")