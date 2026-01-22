# Basic Python Syntax Examples
# These are used to illustrate fundamental Python syntax and constructs.

# Types of Variables
x = 5           # Integer
y = 3.14        # Float
name = "Alice"  # String
is_active = True # Boolean

# Type Casting
x_str = str(x)          # Integer to String
y_int = int(y)          # Float to Integer
is_active_str = str(is_active)  # Boolean to String
# Print variable types
print(type(x_str), type(y_int), type(is_active_str))

# Arithmetic Operations
sum_result = x + y
diff_result = x - y
prod_result = x * y
div_result = x / y
mod_result = x % 2
exp_result = x ** 2
floor_div_result = x // 2

# Print results
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Division:", div_result)
print("Modulus:", mod_result)
print("Exponentiation:", exp_result)
print("Floor Division:", floor_div_result)

# Lists (Arrays)
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

# Indexing and Slicing
# Indexing: Accessing elements
first_number = numbers[0]
last_fruit = fruits[-1]
# Slicing: Sub-Array from index 1 to 3
print(numbers[1:4]) 

# Dictionaries (Hash Maps)
person = {
    "name": "Bob",
    "age": 30,
    "is_student": False
}

# Accessing dictionary values
person_name = person["name"]
person_age = person.get("age")
print("Name:", person_name)
print("Age:", person_age)

# Classes and Objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
my_dog = Dog("Buddy", 3)

print(my_dog.name)  # Accessing attribute
print(my_dog.bark())  # Calling method

# Common Built in Functions and Methods 
numbers = [10, 20, 30, 40, 50]
name = "charlie"
x, y, z = 13, 14, 20

# Length
length_of_numbers = len(numbers)
print("Length of numbers list:", length_of_numbers)

# Min, Max, Avg, Absolute, Rounding
min_number = min(x, y, z)
max_number = max(x, y, z)
avg_number = (x + y + z) / 3
abs(-10)  # Absolute value
round(3.14159, 2)  # Rounding to 2 decimal places
print("Min:", min_number)
print("Max:", max_number)
print("Avg:", avg_number)


# User Input
user_input = input("Enter something: ")
print("You entered:", user_input)

upper_name = name.upper()
print("Uppercase name:", upper_name)
max("apple", "banana", "cherry")  # Lexicographical max

# Boolean Logic
# And: && , Or: || , Not: !
# Greater than: > , Less than: < , Equal to: == , Not equal to: !=
# Greater than or equal to: >= , Less than or equal to: <=

# Logical Operators
# The computer will evaluate the expressions before
# and: True if both operands are true
result_and = (x > 10) and (y < 20)  # True
# or: True if at least one operand is true
result_or = (x < 10) or (y < 20)    # True
# not: Inverts the boolean value
result_not = not (x > 10)           # False


# Strings are case sensitive

username = input("Pick a username: ")
# Usernames must have at least one character.
is_empty = username == ""
print("Is your username empty? " + str(is_empty))
# Your username can't be the same as mine.
is_available = username != "the_real_kim"
print("Is your username available? " + str(is_available))
# The list of usernames is displayed alphabetically.
comes_first = username < "the_real_kim"
print("Does your username come before mine? " + str(comes_first))
# Usernames must have 5 or more characters.
has_min_chars = len(username) >= 5
print("Is your username at least 5 characters long? " + str(has_min_chars))

# Conditional Statements

# If-Else
# Intitialize a variable before using it to ensure it exists in all spaces
# example:

order = "Pad thai"
protein = "" # Initialize protein variable
if order == "Pad thai":
    price = 8.50
    protein = input("Choose a protein (chicken, tofu, shrimp): ")
    if protein == "chicken":
        price += 2.00
    elif protein == "tofu":
        price += 1.50
    elif protein == "shrimp":
        price += 3.00
    else:
        print("Sorry, we don't have that protein option.")
else:
    price = 5.00  # Default price for other orderR
print("Your total is: $" + str(price))

# For Loop: Used for iterating over a sequence (like a list, tuple, dictionary, set, or string)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# harder example
total = 0
prices = [2.5, 3.0, 4.75, 1.25]
for price in prices:
    total += price
print("Total price:", total) 

# While Loop: Repeats as long as a certain boolean condition is met
count = 0
while count < 5:
    print("Count is:", count)
    count += 1 # Increment count to avoid infinite loop
# Continue and Break
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # Skip even numbers
    if n > 7:
        break     # Exit loop if n is greater than 7
    print(n)


# Function Definition
def squareroot(n):
    root = n/2    #initial guess will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + (n / root))

    return root

# Python Match 
"""
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
"""
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

# Python functions with Positional and Keyword Arguments
# Positional Arguments: Arguments that need to be in a specific order
# Keyword Arguments: Arguments that are passed by explicitly naming each parameter and its value

def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")    

greet("Alice")                # Uses default msg
greet("Bob", msg="Hi")        # Uses custom msg

# Python Args and Kwargs: Used to pass a variable number of arguments to a function
# Can be used to handle functions with unknown number of arguments: Doesnt have to be *args and **kwargs specifically, can use any names but * and ** are required
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
display_info(1, 2, 3, name="Alice", age=30)

# Python Decorators: Used to modify the behavior of a function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function
@decorator_function
def display():
    print("Display function executed")

display()


# Python Lambda Functions: Helpful for small, throwaway functions: Benefit is that they can be defined in a single line
# Syntax: lambda arguments: expression

# Example 1: Simple lambda function to multiply two numbers
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Example 2: Using lambda with map(), maps a function to all items in an iterable
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Example 3: Using lambda with filter(), filters items if theyre divisible by 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Example 4: Using lambda with sorted(), sorts a list of words by their length
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)