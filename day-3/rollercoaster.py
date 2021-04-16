# -*- Encoding: UTF-8 -*-

print("Welcome to the rollercoaster!")


def height_check():

    price = 0
    height = int(input("What is your height in centimeters?\n: "))
    age = int(input("How old are you?\n: "))
    mid_life_crisis = 45 <= age <= 55

    if height >= 120:

        print("You are tall enough to ride on the coaster.")

        if age < 12:
            price += 5
            print(f"For your age the price is ${price}")
        elif age <= 18:
            price += 7
            print(f"For your age the price is ${price}")
        elif mid_life_crisis:
            print("Your ride's are free")
        else:
            price += 12
            print(f"For your age the price is ${price}")
    else:
        print("You are not tall enough to ride.")

    if mid_life_crisis:
        photo = str(input("A photo is free but you still get to choose whether you want one or not. Y or N\n: ").upper)
        if photo == "Y":
            pass
        print("Your ride is completely free!")
    else:
        photo = str(input("Would you like a photo? It is an extra 3$. Y or N\n: ").upper())
        if photo == "Y":
            price += 3
            print(f"That brings your total due to ${price}")


def main():
    height_check()


main()
