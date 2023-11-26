def f(name):
  split = str(name).split(" ")

  text = ""

  for word in split:
    text += word[0]

  return text