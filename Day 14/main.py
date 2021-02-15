import random

import art
import game_data
import grey


def dictionary_delete(accounts, to_delete):
    print(to_delete)
    accounts.remove(to_delete)


def higher(a, b):
    """Takes two integers as input's named a and b then returns a lowercase string of either 'a' or 'b' depending on
    which was higher"""
    number = a * (a > b) + b * (a <= b)
    if number == a:
        return 'a'
    else:
        return 'b'


def select_new_comparison(accounts):
    return random.choice(accounts)


def compare():
    """Is the main comparison function of this game. Can be run standalone, does not require main() to be run to
    function correctly."""
    resume = True
    while resume is True:
        accounts = game_data.data.copy()
        current_compare = select_new_comparison(accounts=accounts)
        score = 0
        failed = False
        won = False
        while failed is False and won is False:

            if len(accounts) < 2:
                print("You win, there are no more items for you to guess now.")
                won = True
                continue

            current_against = select_new_comparison(accounts)
            higher_comparison = higher(current_compare['follower_count'], current_against['follower_count'])

            print(f"{art.logo}\n")

            if score != 0:
                print(f"You're Right! Your current score is {score}\n")
            else:
                print(f"Welcome. Your score will show here on your second round.\n")

            print(f"Compare A: {current_compare['name']}, a {current_compare['description']} from "
                  f"{current_compare['country']}\n")
            print(art.vs)
            print(f"Against B: {current_against['name']}, a {current_against['description']} from "
                  f"{current_against['country']}")

            choice = input("\nWho has more follower's? Type 'A' or 'B': ").lower()

            if higher_comparison == 'a' and choice == 'b' or higher_comparison == \
                    'b' and choice == 'a':
                grey.clear()
                print(f"{art.logo}\nUnfortunately you chose incorrectly.\nYour final score was {score}.\n")
                failed = True
                continue

            print("You guessed correctly, well done.")
            score += 1

            if choice == 'a':
                to_delete = current_against
                dictionary_delete(accounts=accounts, to_delete=to_delete)
            else:
                to_delete = current_compare
                dictionary_delete(accounts=accounts, to_delete=to_delete)
                current_compare = current_against

        while True:
            choice = str(input("Would you like to play again?\nAnswer with 'y' or 'n'").lower())
            if choice == 'n':
                resume = False
                break
            elif choice == 'y':
                break
            else:
                print("Please enter a valid input.")


if __name__ == '__main__':
    compare()
