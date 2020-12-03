# -*- Encoding: UTF-8 -*-

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, separated by a comma. ")
names = namesAsCSV.split(", ")

print(f"Today {names[random.randint(0 , len(names) - 1)]} is paying.")
