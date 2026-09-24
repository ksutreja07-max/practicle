def factorial(num):
    if num < 0:
        return "Factorial is not possible for negative number"

    if num == 0 or num == 1:
        return 1

    return num * factorial(num - 1)


number = int(input("Enter a number: "))
print(factorial(number))


def fibonacci(num):
    if num <= 0:
        return 0

    if num == 1:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)


number = int(input("Enter fibonacci number: "))

print(fibonacci(number))

for i in range(number):
    print(fibonacci(i), end=" ")


square = lambda x: x * x

number = int(input("Enter a number: "))
print(square(number))


numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]

odd_num = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_num)
print(max(numbers))
print(min(numbers))


largest = lambda a, b, c: max(a, b, c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(largest(a, b, c))