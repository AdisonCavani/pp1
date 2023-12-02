import json

with open("data.json") as file:
    data = json.load(file)

for arr in data:
    for key, value in arr.items():
        print(f"{key}: {value}")
