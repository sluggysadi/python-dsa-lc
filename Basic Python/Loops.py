# Day 5
# Python Loops

# For loop
#for item in list_of_items:
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits: #Assigning variable name to each of the items in the list
    print(fruit)
    print(fruit + " pie")
print(fruits)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
total_exam = sum(student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

# Range function
total = 0
for number in range(1, 101):
    total += number
print(total)

# Print numbers range 1-100, print Fizz when number is divisible by 3, Buzz, 
# when divisible by 5, and Fizzbuzz when divisible by both
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0: 
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Day 5 Project: PyPassword Generator
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters) 
for symbol in range(1, nr_symbols+1):
    password += random.choice(symbols)
for num in range(1, nr_numbers + 1):
    password += random.choice(numbers) 
print (password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for num in range(1, nr_numbers + 1):
    password_list.append(rndom.choice(numbers)) # type: ignore
print(password_list)

#How do we reorder a list in python?

# 1) using a for loop uses your order though
# my_order = [1, 3, 5, 6, 8, 7, 2, 4]
# password_list = [password_list[i] for i in my_order]
# print(password_list)
# 2) Using shuffle function
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(password)

# Day 6: While loops & functions
import math
anumber = int(input("Please enter an integer "))
try:
       print(math.sqrt(anumber))
except:
       print("Bad Value for square root")
       print("Using absolute value instead")
       print(math.sqrt(abs(anumber)))
# OR

if anumber < 0:
   raise RuntimeError("You can't use a negative number")
else:
   print(math.sqrt(anumber))
