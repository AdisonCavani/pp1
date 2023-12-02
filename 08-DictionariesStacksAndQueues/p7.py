person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
}

print(f"a. {person}")
print(f"b. {person['name']}")
print(f"c. {person['hobby']}")
person["surname"] = "Nowak"
person["married"] = not person["married"]
person["gender"] = "male"
person["hobby"] = person["hobby"] + ["bicycle"]
person["phone"]["work"] = "313131444"

print(person)