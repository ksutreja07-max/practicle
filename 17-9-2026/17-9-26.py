print("Q1. Set Operations")

numbers = {10, 20, 20, 30, 40}
num = [10, 20, 20, 30, 40]
num_tuple = (10, 20, 20, 30, 40)

print(numbers)
print(num)
print(num_tuple)

numbers.add(50)
numbers.remove(10)

print(numbers)

print("Is 10 Present?", 10 in numbers)

num = [10, 20, 30, 30, 40, 50, 50]

set_num = set(num)
list_num = list(set_num)

print(list_num)


print("Q2. Dictionary")

student = {
    "name": "Rahul",
    "age": 21,
    "grade": "B"
}

print(student["name"])

student["city"] = "Junagadh"

del student["age"]

print(student)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key in student.keys():
    print(f"{key} : {student[key]}")


print("Dictionary From List")

keys = ["id", "name", "email"]
values = [201, "Rohan", "rohan@gmail.com"]

employee = {}

for i in range(len(keys)):
    employee[keys[i]] = values[i]

print(employee)


numbers = [15, 25, 35, 45, 55]

print(numbers)

del numbers[2]

print(numbers)


print("Student Management System")

students = [
    {"id": 201, "name": "Neha", "score": 82},
    {"id": 202, "name": "Karan", "score": 78},
    {"id": 203, "name": "Mehul", "score": 91}
]

print(students)

for i in students:
    print(i["name"])