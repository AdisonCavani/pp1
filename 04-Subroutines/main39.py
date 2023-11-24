def f(sentence):
  string = ""

  for letter in sentence:
    if letter != " ":
      string += letter

  # or
  # return sentence.replace(" ", "")

  return string

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))