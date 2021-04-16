# -*- Encoding: UTF-8 -*-

def bmi_calculator():
    print("Welcome to TWB-BMI Calculator.")
    weight = float(input("Weight in Kilograms.\n: "))
    height_in_cm = float(input("Height in Centimeters.\n: "))
    height_in_m_squared = ((height_in_cm / 100) ** 2)
    bmi = float(weight / height_in_m_squared)
    if bmi <= 18.5:
        print(f"Your BMI is {round(bmi, 1)}, you are underweight.")
    elif bmi <= 25:
        print(f"Your BMI is {round(bmi, 1)}, you have a normal weight.")
    elif bmi <= 30:
        print(f"Your BMI is {round(bmi, 1)}, you are slightly overweight.")
    elif bmi <= 35:
        print(f"Your BMI is {round(bmi, 1)}, you are obese.")
    else:
        print(f"Your BMI is {round(bmi, 1)}, you are clinically obese.")


bmi_calculator()
