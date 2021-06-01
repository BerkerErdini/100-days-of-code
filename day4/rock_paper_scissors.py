import random

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
print("Welcome to Rock Paper Scissors!\n")

user = int(input("What do you choose? Enter 0 for Rock, 1 for Paper or 2 for Scissors: "))
cpu = random.randint(0,2)

print("Your choice:")
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)

print("Computer's choice:")
if cpu == 0:
    print(rock)
elif cpu == 1:
    print(paper)
elif cpu == 2:
    print(scissors)

if user == cpu:
    print("It's Tie!")
elif user == 0:
    if cpu == 1:
        print("Computer Wins!")
    elif cpu == 2:
        print("You win!")
elif user == 1:
    if cpu == 0:
        print("You win!")
    elif cpu == 2:
        print("Computer Wins!")
elif user == 2:
    if cpu == 0:
        print("Computer Wins!")
    if cpu == 1:
        print("You win!")



