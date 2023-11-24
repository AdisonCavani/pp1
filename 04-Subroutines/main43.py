def f(name):
  acronym = ""

  for word in str(name).split(" "):
    acronym += word[0]

  return acronym

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))