# -*- Encoding: UTF-8 -*-

import random
import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def while_loop_main(display, hangman_art, word_length, chosen_word, death):

    display_count = display.count("_")

    while display_count != 0:

        if death == 6:
            print("You Lose! Try Again.")
            time.sleep(20)
            quit()

        guess = input("Guess a letter from a to z.\n: ").lower()

        clear()

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in display:
            death = death + 1

        print(display)

        print(hangman_art[death])
        print('')
        print(f"Your life count is {6 - death}")
        print('')

        display_count = display.count("_")

    print("You Win!")
    print(f"The word was: {display}")
    time.sleep(20)


def step_1():
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
    display = []
    death = 0

    for n in range(word_length):
        display.append("_")

    while_loop_main(display, hangman_art, word_length, chosen_word, death)


step_1()
