import csv

arr = []

with open("studentslist.txt", "r") as file:
  reader = csv.reader(file)

  for i, row in enumerate(reader):
    if i > 1 and int(row[2]) < 30:
      arr += [row]

for people in arr:
  print(f"{people[0]}\t{people[1]}\t{people[4]}")