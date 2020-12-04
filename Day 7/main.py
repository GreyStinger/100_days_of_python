# -*- Encoding: UTF-8 -*-

import random
import os
import time
import hangman_art
import hangman_words


def main():

    stages = hangman_art.stages

    word_list = hangman_words.word_list

    chosen_word = list(random.choice(word_list))
    word_length = len(chosen_word)
    display_list = []
    death = 0

    for _ in range(word_length):
        display_list += "_"

    while_loop_main(display_list, stages, word_length, chosen_word, death)


def while_loop_main(display_list, stages, word_length, chosen_word, death):

    display = ""
    guessed_words = ""

    while display_list.count("_") != 0 and death != 6:
        display = ""

        guess = input("Guess a letter from a to z.\n: ").lower()

        clear()

        guessed_words += guess + '-'

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display_list[position] = letter

        if guess not in display_list:
            death = death + 1

        for letter in display_list:
            display += letter

        print(display)

        print(stages[death])
        print('')
        print(f"Your life count is {6 - death}")
        print('')
        print(f"Your guessed words are {guessed_words}")

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
