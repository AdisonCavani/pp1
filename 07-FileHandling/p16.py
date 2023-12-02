file_name = input("File name: ")

with open(file_name, "r") as file:
    line_count = 0

    for _ in file:
        line_count += 1

    print(f"Number of lines: {line_count}")
