binary = input("Enter binary number: ")

decimal = int(int(binary[3]) * pow(2, 0) + int(binary[2]) * pow(2, 1) + int(binary[1]) * pow(2, 2) + int(binary[0]) * pow(2,3))

print(f"Binary number in decimal notation: {decimal}")