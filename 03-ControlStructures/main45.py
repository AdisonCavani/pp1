limit = int(input("Enter n: "))

def isPrime(n):
  if n <= 1:
    return False

  dividers = 0

  for i in range(1, n + 1):
    if n % i == 0:
      dividers += 1

    if dividers > 2:
      return False
  
  return True

print("Prime numbers:", end="")

for i in range(1, limit + 1):
  if isPrime(i):
    print(f" {i}", end="")