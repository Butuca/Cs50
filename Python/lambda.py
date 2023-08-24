people = [
    {"name": "Harry", "house": "gryffindor"},
    {"name": "cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]



people.sort(key=lambda person: person["name"])

print(people)