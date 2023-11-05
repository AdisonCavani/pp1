def read_number():
    return int(input("Enter a number: "))

if __name__ == "__main__":
    num1 = read_number()
    num2 = read_number()

    print(f"{num1} + {num2} = {num1 + num2}")