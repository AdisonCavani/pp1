text = "To be, or not to be, that is the question"
count = 0

for char in text:
  if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    count += 1

print(count)