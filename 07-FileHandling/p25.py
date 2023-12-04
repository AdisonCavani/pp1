import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\\d{2}", message)

sum = 0

for num in temperatures:
  sum += int(num)

print(f"Average temperature: {sum / len(temperatures)}C")