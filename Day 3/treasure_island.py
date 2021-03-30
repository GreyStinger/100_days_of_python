# -*- Encoding: UTF-8 -*-

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = str(input("You come to a crossroads. Would you like to go 'left' or 'right'?\n: ").lower())

if direction != "left":
    print("Game Over! You fell into a trap.")
    quit()

swim_wait = str(input("You come to a large river, do you choose to 'wait' for a boat or 'swim' across the river? \n: ")
                .lower())

if swim_wait != "wait":
    print("Game Over! You got eaten by crocodiles.")
    quit()

door = str(input("You come to a split with 3 different doors, one 'red', one 'yellow', one 'blue'. Which door do you"
                 "wish to go through?\n: ").lower())

if door != "yellow":
    print("Game Over! The room was trapped.")
    quit()

print("Congratulations you win!")
