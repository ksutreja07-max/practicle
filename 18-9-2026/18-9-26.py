# Sets, Dictionary, Type Conversion, List of Dictionary

print("Q1. Set Operations")

numbers = {10, 20, 20, 30, 40}
num_list = [10, 20, 20, 30, 40]
num_tuple = (10, 20, 20, 30, 40)

print(numbers)
print(num_list)
print(num_tuple)

numbers.add(50)
numbers.remove(10)

print(numbers)

print("Is 10 Present?", 10 in numbers)

num_list = [10, 20, 30, 30, 40, 50, 50, 60]

unique_numbers = set(num_list)
new_list = list(unique_numbers)

print(new_list)


print("Q2. Dictionary")

student = {
    "name": "Rohan",
    "age": 21,
    "grade": "B"
}

print(student["name"])

student["city"] = "Junagadh"

del student["age"]

print(student)

for key in student:
    print(key)

for value in student.values():
    print(value)

for key in student:
    print(f"{key} : {student[key]}")


print("Dictionary From List")

keys = ["roll_no", "name", "email"]
values = [201, "Raj", "raj@gmail.com"]

employee = {}

for i in range(len(keys)):
    employee[keys[i]] = values[i]

print(employee)


numbers = [10, 20, 30, 40, 50]

print(numbers)

del numbers[3]

print(numbers)


print("Student Management System")

students = [
    {"id": 201, "name": "Neha", "score": 86},
    {"id": 202, "name": "Karan", "score": 72},
    {"id": 203, "name": "Mehul", "score": 94}
]

print(students)


for student in students:
    print(student["name"])


total_score = 0

for student in students:
    total_score += student["score"]

average_score = total_score / len(students)

print("Average Score:", average_score)


students.append({
    "id": 204,
    "name": "Riya",
    "score": 81
})

print("\nStudent Added Successfully.")
print(students)


for student in students:
    if student["id"] == 203:
        student["score"] = 78

print(students)


for student in students:
    if student["score"] > 80:
        print(student["name"], "--", student["score"])


students.sort(key=lambda x: x["score"], reverse=True)

print(students)


highest_score = students[0]

for student in students:
    if student["score"] > highest_score["score"]:
        highest_score = student

print("Highest Score Student:", highest_score["name"])


grade_count = {
    "A": 0,
    "B": 0,
    "C": 0
}

for student in students:

    score = student["score"]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"

    grade_count[grade] += 1

    print("Name:", student["name"])
    print("Score:", score)
    print("Grade:", grade)

print(grade_count)