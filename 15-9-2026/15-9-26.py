
print("=" * 40)
print("Collection Datatypes")
print("=" * 40)


# List

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print(fruits)

# Access values
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-3])


# Access values using loop

for fruit in fruits:
    print(fruit)


# Add a new value

fruits.append("Kiwi")
print(fruits)


# Remove a value

fruits.pop()
print(fruits)


# Sort the list

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)


# Tuple

numbers = (10, 20, 30, 40, 50)

print(numbers)

print(numbers[0])
print(numbers[1])


# Access tuple values using loop

for number in numbers:
    print(number)


# Tuple values cannot be changed
# numbers[0] = 100


# List Comprehension

square_values = []

for number in range(1, 11):
    if number % 2 == 0:
        square_values.append(number ** 2)

print(square_values)


# List comprehension with range

squares = [number ** 2 for number in range(1, 11)]

print(squares)


# Odd numbers using list comprehension

odd_numbers = [number for number in range(1, 20) if number % 2 != 0]

print(odd_numbers)


# List comprehension using an existing list

numbers = list(range(1, 20))

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)