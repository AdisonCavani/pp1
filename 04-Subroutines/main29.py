def f(amount_to_pay):
  count = 0

  while amount_to_pay >= 5:
    amount_to_pay -= 5
    count += 1

  while amount_to_pay >= 2:
    amount_to_pay -= 2
    count += 1

  while amount_to_pay >= 1:
    amount_to_pay -= 1
    count += 1

  return count

print(f(23))
print(f(8))
print(f(2))
print(f(0))