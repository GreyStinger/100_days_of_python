# -*- Encoding: UTF-8 -*-

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N\n: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N\n: ").upper()
bill = 0

if size == "S":
    bill += 15
if size == "M":
    bill += 20
if size == "L":
    bill += 25
else:
    print("Please try again and enter a valid input.")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
