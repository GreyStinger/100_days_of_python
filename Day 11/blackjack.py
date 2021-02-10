import random
import time

import art
import grey


def card_pick():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, len(cards) - 1)]


def main():
    continue_on = True

    while continue_on:

        player_card_list = [card_pick(), card_pick()]
        player_total = player_card_list[0] + player_card_list[1]
        player_card_draw = True
        computer_card_list = []
        computer_total = 0
        while computer_total <= 17:
            computer_card_pick = card_pick()
            computer_card_list.append(computer_card_pick)
            computer_total += computer_card_pick

        while player_card_draw:
            grey.clear()
            print(f"{art.logo}\nWelcome To Blackjack\n")
            print(f"Your Cards are {player_card_list}. Your total score is now {player_total}\n")
            print(f"The computer's first card is a {computer_card_list[0]}\n")
            player_card_next = str(input("Would you like to draw another card? 'Yes' or 'No': ").lower())
            if player_card_next == "yes":
                iterate = 2
                player_card_list.append(card_pick())
                player_total += player_card_list[iterate]
                print(f"\nYou draw another card.\n")
                time.sleep(1)
                print(f"You draw a {player_card_list[iterate]}. Your total score is now {player_total}\n")
                iterate += 1
                time.sleep(3)
            elif player_card_next == "no":
                print("\nYou Stand.\n")
                time.sleep(3)
                player_card_draw = False
            else:
                print("\nPlease enter a valid input.\n")
                time.sleep(4)
                grey.clear()
                print(f"{art.logo}\nWelcome To Blackjack\n")
                print(f"Your Cards are {player_card_list}. Your total score is now {player_total}\n")
                print(f"The computer's first card is a {computer_card_list[0]}\n")

        grey.clear()

        print(f"{art.logo}\n")
        print(f"Your final hand is {player_card_list}, with a final score of {player_total}.\n")
        print(f"The computers final hand is {computer_card_list}, with a final score of {computer_total}.\n")

        if player_total > 21:
            print("You went over you loose.\n")
        elif computer_total > 21:
            print("The computer went over you win.\n")
        elif player_total > computer_total:
            print("You win.\n")
        elif player_total == computer_total:
            print("It is a draw.\n")
        else:
            print("The computer scored higher. You loose.\n")

        while True:
            play_again = str(input("Would you like to play again? 'Yes' or 'No': ").lower())
            grey.clear()
            if play_again == "yes":
                break
            elif play_again == "no":
                continue_on = False

                break
            else:
                print("\nPlease enter a valid input.\n")

    print("Goodbye then, I hope to see you again soon.")
    time.sleep(3)


if __name__ == '__main__':
    main()
