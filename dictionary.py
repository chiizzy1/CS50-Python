# students = {
#     "Harry": "Gryffindor",
#     "Hermione": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

# for student in students:
#     print(f"{student} is in {students[student]} house")


students = [
    {"name": "Harry", "house": "Gryffindor", "patronous": "Otter",},
    {"name": "Hermione", "house": "Gryffindor", "patronous": "Stag",},
    {"name": "Ron", "house": "Gryffindor", "patronous": "Jack Russel Terrier",},
    {"name": "Draco", "house": "Slytherin", "patronous": None,}
]

for student in students:
    print(f"{student['name']} is in {student['house']} house and has a patronous of {student['patronous']}")