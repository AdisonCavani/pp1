def f(text):
  string = ""

  for char in text:
    string += char + "-"

  return string[:-1]

print(f("University"))
print(f("UE"))
print(f("x"))
print(f(""))
