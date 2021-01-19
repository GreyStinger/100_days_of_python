# -*- Encoding: UTF-8 -*-

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime is True:
        print("This number is Prime")
    else:
        print("This number is not Prime")


n = int(input("Check this number: "))
prime_checker(number=n)
