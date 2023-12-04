with open("grades.txt", "r") as file:
  for i, line in enumerate(file):
    if i == 1:
      text = line

text = text.replace("Grades: ", "").split(", ")

sum = 0

for num_str in text:
  sum += float(num_str)

print(f"Arithmetic mean: {round(sum / len(text), 2)}")