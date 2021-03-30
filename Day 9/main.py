# -*- Encoding:UTF-8 -*-

from grey import clear
from art import logo


def main():
    secret_auction_dictionary = {}
    top_bidder = ["default", 0]
    more_bidders = True
    while more_bidders:
        print(logo)
        print("The secret auction.\n")
        name = input("Please enter your name: ")
        amount = int(input("Please enter your bid: $"))
        secret_auction_dictionary[name] = amount
        if secret_auction_dictionary[name] > top_bidder[1]:
            top_bidder = [name, secret_auction_dictionary[name]]
        if input("Are there more bidders? Please answer with 'yes' or 'no'.\n").lower() == "no":
            more_bidders = False
        clear()
    print(f"The highest bidder was {top_bidder[0]} with a bid of ${top_bidder[1]}.")


main()
