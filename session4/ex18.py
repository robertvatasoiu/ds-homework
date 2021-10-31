"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""


def sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum(numbers[1:])


print(sum([1, 2, 3]))
