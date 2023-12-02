with open("MeatAndFish.txt", "r") as file1:
    with open("GrainsAndBread.txt", "r") as file2:
        with open("allproducts.txt", "a") as new_file:
            content = file1.read() + file2.read()
            new_file.write(content)