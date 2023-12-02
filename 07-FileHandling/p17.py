with open("17.txt", "r") as file:
    content = file.read().split("\n")
    
    counter = 0
    lines = 1

    while counter != len(content):
        if lines <= 5:
            print(content[counter])
            lines += 1
            counter += 1
        else:
            if input() == "":
                lines = 1
