def f(x: int, y: int, d: str):
  for num in range(x, y + 1):
    num = str(num)

    if num.count(d) > 0:
      return True

  return False

if __name__ == "__main__":
  print(f(10, 15, "14"))
  print(f(100, 120, "11"))
  print(f(205, 210, "04"))