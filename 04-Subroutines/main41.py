def f(n):
  counter = 0
  i = 0

  while True:
    if is_prime(i):
      counter += 1
    
    if counter == n:
      return i

    i += 1

def is_prime(n):
  if n <= 1:
    return False
  
  dividers = 0

  for i in range(1, n + 1):
    if dividers > 2:
      return False
    
    if n % i == 0:
      dividers += 1

  if dividers == 2:
    return True

  return False

print(f(1))
print(f(5))