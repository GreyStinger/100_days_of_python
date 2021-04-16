# -*- Encoding: UTF-8 -*-

def leap_year_calculation():
    year = int(input("Enter the year you wish to asses\n: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("The year is a leap year. It has 366 days.")
            else:
                print("The year is not a leap year it has 365 days.")
        else:
            print("The year is a leap year. It has 366 days.")
    else:
        print("The year is not a leap year. It has 365 days.")


leap_year_calculation()
