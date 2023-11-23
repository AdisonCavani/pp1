import main21_mymath
import main20_mykeyboard

number = main20_mykeyboard.read_number()
random = main21_mymath.generate_number()

if number == random:
  print("You won the game!!")
else:
  print("You lost")