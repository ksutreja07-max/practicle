count = 0

def my_count():
    global count
    count += 1
    print("Function called:", count)

my_count()
my_count()
my_count()


total = 0

def add_number(number):
    global total
    total += number

n = int(input("How many numbers do you want to enter: "))

for i in range(n):
    number = int(input(f"Enter number {i + 1}: "))
    add_number(number)

print("Total:", total)


username = "VIP Guest"

def change_name(name):
    global username
    username = name

print("Before:", username)

new_name = input("Enter new username: ")
change_name(new_name)

print("After:", username)


def operations(numbers):
    total = sum(numbers)
    highest = max(numbers)
    lowest = min(numbers)

    return total, highest, lowest


numbers = [10, 20, 30, 40, 50]

total, highest, lowest = operations(numbers)

print("Total:", total)
print("Maximum:", highest)
print("Minimum:", lowest)


def split_string(text):
    vowels = ""
    remaining = ""

    for char in text:
        if char.lower() in "aeiou":
            vowels += char
        else:
            remaining += char

    return vowels, remaining


text = input("Enter a string: ")

vowels, remaining = split_string(text)

print("Vowels:", vowels)
print("Remaining:", remaining)


def prime(number, divisor=2):
    if number < 2:
        return False

    if divisor == number:
        return True

    if number % divisor == 0:
        return False

    return prime(number, divisor + 1)


def print_prime(start, end):
    if start > end:
        return

    if prime(start):
        print(start)

    print_prime(start + 1, end)


start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print_prime(start, end)