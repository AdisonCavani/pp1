name = "Anna May"
university = "Krakow University of Economics"
field = "Applied Informatics"

file = open("student.txt", "a")
file.write(f"{name}\n{university}\n{field}")

file.close()