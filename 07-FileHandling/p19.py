with open("17.txt", "r") as file:
    with open("copylines.txt", "a") as new_file:
        for line in file:
            new_file.write(line)
