def f(player1: str, player2: str):
  counter1 = 0
  counter2 = 0

  for char in player1:
    if char == "A" or char == "K" or char == "Q" or char == "J" or char == "T":
      counter1 += 10
    else:
      counter1 += int(char)
  
  for char in player2:
    if char == "A" or char == "K" or char == "Q" or char == "J" or char == "T":
      counter2 += 10
    else:
      counter2 += int(char)

  return counter1 >= counter2

print(f("AJ972","AQT72"))
print(f("9532","K8"))