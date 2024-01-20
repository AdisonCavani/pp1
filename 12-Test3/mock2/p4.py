def f(fnc, res: list):
  arr = []

  for num in res:
    if fnc(num) == True:
      arr.append(num)

  small = 0
  large = 0

  for idx, num in enumerate(arr):
    if num < small or idx == 0:
      small = num

    if num > large or idx == 0:
      large = num

  return large - small

if __name__ == "__main__":
  res = [95, 90, 20, 50, 70] 

  fnc1 = lambda x: x > 50
  print(f(fnc1, res))

  fnc2 = lambda x: x > 30 and x < 90
  print(f(fnc2, res))