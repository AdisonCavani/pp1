def f(detector):
  last = detector[0]
  count = 0

  for sign in detector:
    if count == 3:
      return True
    
    if sign == last:
      count += 1

    last = sign
  
  return False


print(f("+-+++-+---")) 
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))
