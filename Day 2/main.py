# -*- Encoding: UTF-8 -*-

def split_payment():
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill?\n: R"))
    split_size = int(input("Between how many people is the bill being split?\n: "))
    tip_size = int(input("What percentage tip would you like to give? eg. 10, 15, 20.\n: "))
    per_person_pay = float(total_bill / split_size)
    print(f"Each person should pay R{round((per_person_pay) + ((per_person_pay) * (tip_size / 100)), 2)}")


split_payment()
