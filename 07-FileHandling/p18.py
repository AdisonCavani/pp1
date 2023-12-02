with open("17.txt", "r") as file:
    content = file.read()

    with open("copy.txt", "a") as new_file:
        new_file.write(content)
