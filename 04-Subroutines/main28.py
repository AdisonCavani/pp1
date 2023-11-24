def f(binary_number):
  for i in binary_number:
    if i != "0" and i != "1":
      return False
    
  return True

print(f"f({"101101"}) returns {f("101101")}")
print(f"f({"1311a10100"}) returns {f("1311a10100")}")