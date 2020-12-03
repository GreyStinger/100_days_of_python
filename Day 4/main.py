# -*- Encoding: UTF-8 -*-
import random

rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """

paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """

scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

rock_paper_scissors = [rock, paper, scissors]

human_choice = int(input("Welcome to rock, paper, scissors. Type 1 for rock, type 2 for paper, type 3 for scissors.\n: "))
# computer_choice = int(random.randint(1, 3))
computer_choice = random.randint(1, 3)

print("Your Choice")
print(rock_paper_scissors[human_choice - 1])
print("Computers Choice")
print(rock_paper_scissors[computer_choice - 1])

variable_decision = int(human_choice - computer_choice)

if variable_decision == 0:
    print("Draw")
elif variable_decision == 1 or variable_decision == -2:
    print("You Win")
elif variable_decision == -1 or variable_decision == 2:
    print("Computer Wins")
else:
    print("error")
