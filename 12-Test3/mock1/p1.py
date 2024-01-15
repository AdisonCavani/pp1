def f(word: str):
  string = ""

  for index, _ in enumerate(word):
    xd = ""

    for char in word:
      if char == word[index]:
        xd += char.capitalize()
      else:
        xd += char

    if index == 0:
      string += xd
    else:
      string += f"-{xd}"

  return string

if __name__ == "__main__":
  print(f("book"))
  print(f("water"))
  print(f("ok"))
  print(f("a"))
  print(f(""))