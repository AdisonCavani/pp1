def f(product_code):
  sum = 0

  for char in str(product_code)[:-1]:
    sum += int(char)

  if sum % 7 == int(product_code[3]):
    return True

  return False

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))