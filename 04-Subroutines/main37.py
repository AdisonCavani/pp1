def f(n):
  a = 0
  b = 1

  for _ in range(0, n - 1):
    temp = a + b
    a = b
    b = temp

  return a

print(f(5))
print(f(9))