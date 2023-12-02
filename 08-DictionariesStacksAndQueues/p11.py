import json


movie = {
    "title": "Harry Potter",
    "year": 2000,
    "oscar": False
}

with open("favourite.json", "a") as file:
    file.write(json.dumps(movie, indent=4))