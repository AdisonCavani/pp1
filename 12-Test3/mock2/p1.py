def f(n):
  small = 0
  large = 0
  small_pass = False
  large_pass = False

  for num in str(n):
    num = int(num)

    if (num % 2 == 1 and small_pass == False) or (num % 2 == 1 and num < small):
      small = num
      small_pass = True
    if (num % 2 == 1 and large_pass == False) or (num % 2 == 1 and num > large):
      large = num
      large_pass = True

  if small_pass == False and large_pass == False:
    return -1

  return large - small

if __name__ == "__main__":
  print(f(10852))
  print(f(7235973))
  print(f(4388))
  print(f(846206))