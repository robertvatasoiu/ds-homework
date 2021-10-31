"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }

"""
import random
from random import randint
import string
import json


def func(my_str):
    my_dict = {}
    for i in range(0, 4):
        x = "".join(
            [
                random.choice(string.ascii_letters)
                for i in range(random.choice([3, 4, 5, 6]))
            ]
        )
        number = random.randint(0, 10)
        my_dict[number] = x

    with open(my_str + ".json", "w+") as file:
        json.dump(my_dict, file)


func("ceva")

