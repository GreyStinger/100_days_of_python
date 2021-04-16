# -*- Encoding: UTF-8 -*-

import art
import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)


def variable_allocation():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    cipher(pre_cipher_text=text, shift_amount=shift, encode_or_decode=direction)


def cipher(pre_cipher_text, shift_amount, encode_or_decode):
    post_cipher_text = ""

    for i in pre_cipher_text:
        if i not in alphabet:
            post_cipher_text += i
        else:
            if encode_or_decode == "encode":
                x = alphabet.index(i) + shift_amount
                if x > 25:
                    x = x - 26
                post_cipher_text += alphabet[x]
            else:
                x = alphabet.index(i) - shift_amount
                post_cipher_text += alphabet[x]
    print(f"The {encode_or_decode}d word is {post_cipher_text}")
    restart()


def restart():
    restart_check = input("Would you like to run the program again? Please answer with 'yes' or 'no'.\n").lower()
    if restart_check == "yes":
        variable_allocation()
    elif restart_check == "no":
        print("Goodbye")
        time.sleep(6)
        quit()
    else:
        print("You didn't answer carefully so I am going to quit, but you can always start me again manually.")
        time.sleep(8)
        quit()


variable_allocation()
