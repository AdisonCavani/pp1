def create_2d_arr(x, y):
  return [[0 for _ in range(1, x + 1)] for _ in range(1, y + 1)]

arr = create_2d_arr(3, 5)
print(f"Array: {arr}")