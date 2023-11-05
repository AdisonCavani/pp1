code_str = input("Enter EAN-13 article number: ")

if code_str.__len__ == 13:
    print("Article number is correct")

    if code_str.startswith("590"):
        print("Article manufactured in Poland")
else:
    print("Invalid article number")