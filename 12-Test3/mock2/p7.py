def f(d: list):
  cars = []

  for arr in d:
    if arr[1] == "in":
      cars.append(arr[0])
    if arr[1] == "out":
      cars.remove(arr[0])

  return cars

if __name__ == "__main__":
  cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
  print(f(cars))

  cars1 = [["KR234","in"],["KR234","out"]]
  print(f(cars1))