"""
    Ex. 4: Mai jos aveti 2 functii:
        - add_prefix --> adauga un prefix primit ca parametru unui string
        primit tot ca parametru
        - generate_random_str --> genereaza un string aleator de dimensiune X,
        X fiind un parametru

        Va trebui sa scrieti o functie care sa adauge un sufix (add_suffix),
        dar acel sufix nu trebuie sa contina nicio litera din prefix.

        Sufixul si prefixul le veti primi ca si input de la tastatura, la fel si
        X, care este lungimea stringului aleator.
        In cazul in care sufixul are vreo litera pe care o are si prefixul,
        veti cere un sufix nou, pana cand este dat unul corect, sau pana cand
        a fost incercat de 3 ori. A 4-a oara veti printa stringul fara sufix.
    Rezultatul ar trebui sa arate asa:
        - pentru prefix = 'bla', sufix = 'cmi', x = 3 si un string aleator 'lol'
            ---> 'blalolcmi'
        - pentru prefix = 'bla', sufix = (pe rand, 'ba', 'la', 'bla') x = 3
        si un string aleator 'lol'
            ---> 'blalol'

    Orice e neclar, ma intrebati pe discord la orice ora, fara probleme.
"""
import random


def add_prefix(pfx, rand_str):
    return pfx + rand_str


def add_sufix(sfix, randomstr):
    return randomstr + sfix


# Nu am spus ca stringul generat aleator trebuie sa contina toate literele
def generate_random_str(str_length):
    rand_str = ""
    while str_length:
        str_length -= 1
        rand_str += random.choice(["a", "x", "c", "m", "i"])
    print(f"The generated string is {rand_str}")
    return rand_str


prefix = input("Give me an prefix\n")

sufix = input("Give me a sufix\n")

x = int(input("Give me a number to generate the random string\n"))

# Verific daca sufixul contine litere din prefix
n = 0
for i in sufix:
    for j in prefix:
        if i == j:
            newsfx = input("Inserati un nou sufix\n")
            n += 1

        elif n == 3:
            print("Sufixul nu este bun")
            print(add_prefix(prefix, generate_random_str(x)))
            break

rndmword = generate_random_str(x)


def newword(prefix, rndmword, sufix):
    return prefix + rndmword + sufix


# print(add_prefix(prefix, generate_random_str(x)))


print("The new word is:", newword(prefix, rndmword, newsfx))
# prefix=bla
# x=stral

