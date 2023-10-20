import csv

students = []

with open("more_students_info.csv") as file:
    # reader = csv.reader(file)
    # for name, home in reader:
    #     students.append({"name": name, "home": home})

    
    #  using csv dict reader    
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})       
                
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")