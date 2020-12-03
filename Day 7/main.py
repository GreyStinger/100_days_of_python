# -*- Encoding: UTF-8 -*-

import random
import os
import time


def main():
    hangman_art = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    word_list = ["aardvark", "baboon", "camel"]

    chosen_word = list(random.choice(word_list))
    word_length = len(chosen_word)
    display_list = []
    death = 0

    for n in range(word_length):
        display_list.append("_")

    while_loop_main(display_list, hangman_art, word_length, chosen_word, death)


def while_loop_main(display_list, hangman_art, word_length, chosen_word, death):

    display = ""

    while display_list.count("_") != 0 and death != 6:
        display = ""

        guess = input("Guess a letter from a to z.\n: ").lower()

        clear()

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display_list[position] = letter

        if guess not in display_list:
            death = death + 1

        for letter in display_list:
            display += letter

        print(display)

        print(hangman_art[death])
        print('')
        print(f"Your life count is {6 - death}")
        print('')

    if death == 6:
        print("You Lose! Try Again.")
        time.sleep(20)
        quit()
    else:
        print("You Win!")
        print(f"The word was: {display}")
        time.sleep(20)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


main()
