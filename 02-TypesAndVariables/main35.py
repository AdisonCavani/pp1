import math


circ = int(input("Enter tree circumference: "))

print(f"Tree can be cut down: {(circ / math.pi) >= 50}")