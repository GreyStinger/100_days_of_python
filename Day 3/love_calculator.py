# -*- Encoding: UTF-8 -*-

print("Welcome to the Love Calculator!")
name1 = str(input("What is your name? \n").lower())
name2 = str(input("What is their name? \n").lower())
combined_names = name1 + name2

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")

true = str(t + r + u + e)
love = str(l + o + v + e)

love_score = int(true + love)

if (love_score <= 10) or (love_score >= 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
