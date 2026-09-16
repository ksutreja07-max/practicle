# Collection Datatypes

# Collection datatypes are used to store multiple values in a single variable. Python provides several collection types, including List , Tuple , Set and Disctionary.abs

# List & Tuple
# Mutability of List and Tuple

# A List is an orderd collection of values. MUtability mean the ability of an object to change its contents after it has been decalred / created.

# List comprehension

# List comprehension is a sort and simple structure way to make / create a new list from an old list / existing list  , such as a List , Tuple or range.

print("="*40)

print("List in Python")

# create

fruits =['Apple' , 'Banana' , 'Mango' , 'Orange',  'Grapes']
           

print(fruits)

# Value Eccess

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-3])


# Value Access through loop

print("Value Access through loop")

for fruit in fruits:
  print(fruit)

# Add New Value

# Python New Value Adding : Built-in Function (append())

fruits.append("Kiwi")

print(fruits)

# Remove value from List

# Built-in Function : pop()

# fruits.pop(0)
# fruits.pop()
# fruits.pop()

# print(fruits)

# Sorting (sort())

fruits.sort()

print(fruits)

fruits.sort(reverse=True)

print(fruits)

# Tuple

# create

numbers = (10 , 20 , 30 , 40 , 50)

print(numbers)

# Access value from tuple individual

print(numbers[0])
print(numbers[1])

# Access value from tuple using loop

for num in numbers:
  print(num)

numbers = [10, 20, 30, 40, 50]

numbers[0] = 1

print(numbers)







