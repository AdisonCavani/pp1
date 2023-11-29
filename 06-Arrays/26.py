arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name = ""

for item in arr:
  if len(item) > len(longest_name):
    longest_name = item

print(f"Longest name: {longest_name}")