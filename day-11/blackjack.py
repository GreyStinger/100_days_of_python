import random
import time

import art
import grey


def card_pick():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def main():
    continue_on = True

    while continue_on:

        player_card_list = [card_pick(), card_pick()]
        player_total = sum(player_card_list)

        player_card_draw = True
        dealer_card_list = []
        dealer_total = 0

        while dealer_total <= 17:
            dealer_card_pick = card_pick()
            dealer_card_list.append(dealer_card_pick)
            dealer_total += dealer_card_pick

        if player_total == 21:
            player_total = 0

        if dealer_total == 21:
            dealer_total = 0

        while player_card_draw:

            grey.clear()

            print(f"{art.logo}\nWelcome To Blackjack\n")

            if player_total == 0:
                print(f"Your Cards are {player_card_list}. You have a blackjack.")
                time.sleep(3)
                break
            else:
                print(f"Your Cards are {player_card_list}. Your total score is now {player_total}\n")
                print(f"The dealer's first card is a {dealer_card_list[0]}\n")

            player_card_next = str(input("Would you like to draw another card? 'Yes' or 'No': ").lower())

            if player_card_next == "yes":

                iterate = 2
                player_card_list.append(card_pick())
                player_total = sum(player_card_list)

                print(f"\nYou draw another card.\n")

                time.sleep(1)

                print(f"You draw a {player_card_list[iterate]}. Your total score is now {player_total}\n")

                iterate += 1

                if 11 in player_card_list and player_total > 21:
                    player_card_list[player_card_list.index(11)] = 1
                    player_total = sum(player_card_list)
                    print("Your card value went over 21 but you had an ace, so your ace's value has now become 1.")
                    time.sleep(7)
                else:
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
                print(f"The dealer's first card is a {dealer_card_list[0]}\n")

        grey.clear()

        if player_total == 0:
            print("Got a blackjack.")
            if dealer_total == 0:
                print("Unfortunately for you the dealer also got a blackjack.")
        else:
            print(f"{art.logo}\n")
            print(f"Your final hand is {player_card_list}, with a final score of {player_total}.\n")
            if dealer_total == 0:
                print("The dealer got a blackjack.")
            else:
                print(f"The dealers final hand is {dealer_card_list}, with a final score of {dealer_total}.\n")

        if player_total > 21:
            print("You went over you loose.\n")
        elif dealer_total > 21:
            print("The dealer went over you win.\n")
        elif player_total == 0 and dealer_total != 0:
            print("You got a blackjack and you win.")
        elif player_total > dealer_total:
            print("You win.\n")
        elif player_total == dealer_total:
            print("It is a draw.\n")
        else:
            print("The dealer scored higher. You loose.\n")

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
