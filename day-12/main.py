import grey
import random


def pick_difficulty():

    print("\nWhat difficulty would you like to play at? 'Easy' or 'Hard'?\n")
    difficulty = input("Please enter your difficulty: ").lower()

    while True:

        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            difficulty = input("Please enter a valid input:")


def pick_number():
    return random.randint(1, 100)


def guess():

    first_run = True
    continue_on = True

    while continue_on is True:

        if first_run is False:
            print("Welcome back ready for another game?\n\nPress enter to continue. ")
            input()
            grey.clear()

        lives = pick_difficulty()
        number = pick_number()
        lives_finished = False
        number_guessed = False

        if lives == 5:
            print("\nSo you have chosen hard ey??? Well good luck to you.\n")
        else:
            print("\nAhh, so you have taken the easy rout I see.\n")

        print("Anyway, press a key to start guessing.")
        input()

        while lives_finished is False and number_guessed is False:

            print(f"\nYou have {lives} lives left.")

            if lives <= 0:
                print("\nYou ran out of lives. You lose.")
                lives_finished = True
                continue

            user_input = int(input("\nInput your number here: "))

            if user_input > 100:
                print("\nThe number is between 1 and 100.")
                print("\nTry Again")
            elif user_input < 0:
                print("\nThe number is between 1 and 100.")
                print("\nTry Again")
            elif user_input < number:
                print("\nYou guessed to low.")
                print("\nTry Again")
                lives -= 1
            elif user_input > number:
                print("\nYou guessed to high.")
                print("\nTry Again")
                lives -= 1
            elif user_input == number:
                print("\nYou guessed the number, well done.")
                number_guessed = True

        if lives_finished is True:
            while True:
                try_again = input("\nYou have lost would you like to try again?\nPlease answer with 'yes' or 'no': ")
                if try_again == "no":
                    continue_on = False
                    break
                elif try_again == "yes":
                    grey.clear()
                    break
                else:
                    print("Please enter a valid input.")
        elif number_guessed is True:
            while True:
                play_again = input("You win would you like to play again?\nPlease answer with 'yes' or 'no': ")
                if play_again == "no":
                    continue_on = False
                    break
                elif play_again == "yes":
                    grey.clear()
                    break
                else:
                    print("Please enter a valid input.")


def main():

    print("Welcome to greys number guessing game.\nHopefully you will enjoy the game.\n\nPress enter to continue.")
    input()
    start = input("Type 'start' to start the game or type 'quit' to quit it: ").lower()

    while True:

        if start == "start":
            grey.clear()
            guess()
            break
        elif start == "quit":
            break
        else:
            start = input("Please enter a valid input: ")

    print("Goodbye then. Have a Great Day.")


if __name__ == '__main__':
    main()
