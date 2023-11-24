def f(number):
  sum = 0
  string = str(number)

  for number in range(0, 9):
    count = 0

    for letter in string:
      if number == int(letter):
        count += 1
      if number == int(letter) and count > 1:
        sum += number
    
    if count > 1:
      sum += number

  return sum

print(f(1027))
print(f(230335))
print(f(513553007))