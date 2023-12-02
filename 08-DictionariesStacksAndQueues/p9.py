countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 98000000},
    {"name": "France", "population": 78000000},
    {"name": "Ukraine", "population": 28000000},
    {"name": "Russia", "population": 156000000},
]

print("COUNTRY POPULATION")

counter = 0

while counter != len(countries):
    for key, value in countries[counter].items():
        print(value, end="\t")
    print()

    counter += 1
