rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if choice == "0":
    print(rock)
elif choice == "1":
    print(paper)
else:
    print(scissors)

print("Computer chose:\n")

random_choice = random.choice([rock, paper, scissors])

print(f"{random_choice}\n")

if choice == 0 and random_choice == 0:
    print("It's a draw")
elif choice == 0 and random_choice == 1:
    print("You lose")
elif choice == 0 and random_choice == 2:
    print("Yay! You win")
elif choice == 1 and random_choice == 1:
    print("It's a draw")
elif choice == 1 and random_choice == 2:
    print("You lose")
elif choice == 1 and random_choice == 0:
    print("Yay! You win")
elif choice == 2 and random_choice == 0:
    print("It's a draw")
elif choice == 0 and random_choice == 1:
    print("You lose")
else:
    print("Yay! You win")
