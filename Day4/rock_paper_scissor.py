# Rock Paper Scissors

"""
        Game Rules

Rock wins Scissor
Scissor wins Paper
Paper wins Rock
"""

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

rps = [rock, paper, scissors]

choice = int(input("Choose your move! Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)



if choice <= 2 and choice > 0:
    print(rps[choice])
    print("Computer choose:")
    print(rps[computer])

    if choice == computer:
        print("It's a Draw")
    elif choice == 0 and computer == 2:
        print("You wins!")
    elif choice == 2 and computer == 0:
        print("Computer wins!")
    elif choice > computer:
        print("You win!")
    elif choice < computer:
        print("Computer win!")
        
else:
    print("Wrong Input")
