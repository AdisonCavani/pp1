def f(binary_number):
  binary_number = str(binary_number)

  for letter in binary_number:
    if letter != "0" and letter != "1":
      return False
    
  return True