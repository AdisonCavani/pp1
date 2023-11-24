def f(x, y):
  sum = 0

  for num in range(x, y + 1):
    if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
      sum += num

  return sum

print(f(1, 20))
print(f(10, 30))