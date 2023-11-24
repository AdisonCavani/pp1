def f(password):
  password = str(password)
  unique_count = 0

  for char in password:
    if password.count(char) == 1:
      unique_count += 1

  return unique_count >= 6

print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))