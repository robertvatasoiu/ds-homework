"""
    Ex. 5: Scrieti o functie cu un singur parametru (o lista) care sa
    adauge 1 tuturor elementelor din lista.

    Raspunsul corect:
        - func([1, 2, 3])
            ---> [2, 3, 4]

    Observatii:
        - functia trebuie sa fie MAXIM o linie de cod (2, daca luam in calcul
        si definitia functiei)
        - hint: list comprehensions (google it if you don't know it already)
"""


def func(x):
    new_list = [i + 1 for i in x]
    print(new_list)


func([1, 2, 3, 4, 5])

