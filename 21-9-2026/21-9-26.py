# Python Functions

# 1. Built-in Functions vs User-Defined Function
# 2. Arbitrary Arguments
# 3. Keyword Arguments
# 4. __doc__ (Docstrings)


# Q1. Built-in Functions

numbers = [35, 78, 15, 92, 46]

print("Original List:", numbers)
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Sorted:", sorted(numbers))
print("Sum:", sum(numbers))
print("Data Type:", type(numbers))


# User-Defined Function

def welcome(name):
    """Create a welcome message for a person."""
    return f"Hello {name}, Welcome to Python Class."

print(welcome("Rahul"))


# *args : Arbitrary Arguments

def calculate_sum(*args):
    """Add any number of values and return their total."""
    total = 0

    for number in args:
        total += number

    return total

print(calculate_sum(15, 25, 35, 45))


# **kwargs : Keyword Arguments

def student_details(*args, **kwargs):
    """Display positional and keyword arguments."""
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)


student_details("Rahul", 21, 88)
student_details(name="Rahul")


# Product Details using **kwargs

def product_info(**kwargs):
    total = kwargs["price"] * kwargs["quantity"]

    return f"""
Product Name: {kwargs['name']}
Product Price: {kwargs['price']}
Product Quantity: {kwargs['quantity']}
Total: {total}
"""

print(product_info(name="Mobile", price=25000, quantity=2))


# Docstrings

print(welcome.__doc__)
print(calculate_sum.__doc__)