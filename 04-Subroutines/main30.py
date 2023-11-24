def f(number, even):
  sum = 0
  number = str(number)

  for i in number:
    i = int(i)

    if even and i % 2 == 0:
      sum += i
    elif even != True and i % 2 != 0:
      sum += i
      
  return sum
    

print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))
print(f(13115, True))