def f(x: int, y: int, digit: int):
  counter = 0

  for i in range(x, y + 1):
    i = str(i)
    counter += i.count(str(digit))

  return counter

if __name__ == "__main__":
  print(f(10, 15, 1))
  print(f(28, 32, 2))
  print(f(100, 105, 6))
  print(f(100, 101, 0))