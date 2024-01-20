def f(d: dict):
  sum = 0
  count = 0

  for num in d.values():
    sum += num
    count += 1

  avg = sum / count

  occur = 0

  for num in d.values():
    if num > avg:
      occur += 1

  return occur

if __name__ == "__main__":
  print(f({"LO231": 150, "BA787": 120, "NZ15": 30}))
  print(f({"LO231": 150, "BA787": 20, "NZ15": 30}) )