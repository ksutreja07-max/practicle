print("Set Operations")

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

values = [10, 20, 20, 30, 40, 40, 50]

unique_values = set(values)
new_list = list(unique_values)

print(new_list)


print("Dictionary")

student = {
    "name": "Rahul",
    "age": 21,
    "grade": "B"
}

print(student["name"])

student["city"] = "Rajkot"

del student["age"]

print(student)

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key} : {value}")