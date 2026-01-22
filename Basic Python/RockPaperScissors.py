# Day 3-4
# Randomization & Python lists

# Indexing & Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][2])

import random
# Who will pay the bill
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends)) # Option 1
last_value = friends.index(friends[-1]) # Index of last value --> int 
random_index = random.randint(0,last_value) # Option 2
print(friends[random_index])

# Rock Paper Scissors Excercise
# ASCII
rock = (""":
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = (""":
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = (""":
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_images = [rock, paper, scissors]

print("Let's Play Rock Paper Scissors!")
print("--------------------------------")

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors!"))
if user_input >= 0 and user_input <= 2:
    print(f"You chose {game_images[user_input]}")

computer_input = random.randint(0,2)
print(f"Computer chose")
print(game_images[computer_input])

if user_input >= 3 or user_input < 0:
    print("You typed an invalid number. You lose!")
elif user_input == 0 and computer_input == 2:
    print("You win!")
elif user_input == 0 and computer_input == 2:
    print("You lose!")
elif computer_input > user_input:
    print("You lose")
elif computer_input < user_input:
    print("You win!")
elif computer_input == user_input:
    print("Tie!")
else:
    print("Invalid output!")
