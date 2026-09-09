# Topic List

'''

1. String Formatting
2. String Indexing and slicing
3. Case conversion
4. String searching
5. String replacing
6. String counting
7. Split and Join
8. String checking method
9. Removing characters
10. Reverse and Plindrome
11. Escape characters
12. f-string , format() , % formatting

'''

# ====== CREATING STRING ======

name = "Kuldip"
city = 'Junagadh'

print (name)
print (city)

# ====== MULTIPLE STRING ======

message = ''' hello world 
    i am kuldip sutreja 
    from red and white 
    skill education 
         junagadh'''

print (message)

# ====== STRING INDEXING ======

word = "pythonpro"

print (word[0])
print (word[4])
print (word[-2])
print (word[-5])

# ====== STRING SLICING ======

#pythonpro

print (word[0:4])
print (word[3:8])
print (word[:5])
print (word[3:])
print (word[:])
print (word[:-3])
print (word[0::2])
print (word[::-1])

# ======STRING CONCATINATING ======

a = "Kuldip"
b = "Sutreja"

print (a + " " + b)

city = "Junagadh"
state = "Gujarat"

full_Address = city + " " + state

print (full_Address)

# ====== STRING FORMATTING ====== F - STRING ======

name = input ("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current: "))

age = current_year - birth_year 

print (f"Hello {name}!, you are {age} years old.")

# ====== DECIMAL PLACES ======

marks = int(input("Enter your marks: "))
total = int(input("Enter total marks: "))

percentage = marks/total*100

print (f"your percentage is {percentage:.2f}%")

# ====== EXPRESSION INSIDE F - STRING ======

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print (f"sum of {a} and {b} is {a+b}")

# ====== FORMAT () METHOD ======

thing = "watch"
price = 35000

print ("the price of {} is {}".format(thing,price))

# ====== POSITIONAL ARGUEMENTS ======

print ("the price of {0} is {1}".format(thing,price))

# ====== NAMED ARGUEMENTS ======

k = "TV"
c = "samsung"

print ("the company of {b} is {h}".format(b = k , h = c))