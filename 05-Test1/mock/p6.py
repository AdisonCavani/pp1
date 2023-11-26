def f(number, even):
  number = str(number)
  sum = 0

  for letter in number:
    if even == True and int(letter) % 2 == 0:
      sum += int(letter)
    elif even == False and int(letter) % 2 != 0:
      sum += int(letter)

  return sum