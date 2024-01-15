def f(uid: list):
  for i in uid:
    if uid.count(i) > 1:
      return False

  return True

if __name__ == "__main__":
  print(f(["john5", "ann123", "JOHN5", "xxx", "abc333", "a10"]))
  print(f(["abc123", "ann", "abc123", "a10"]))
  print(f(["bob2", "bob2"]))
  print(f(["bob2", "BOB2"]))