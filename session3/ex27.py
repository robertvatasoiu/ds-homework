"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
numberofletters=input()

import random
import string
letters = string.ascii_letters
print(''.join(random.choice(letters) for i in range(int(numberofletters))))