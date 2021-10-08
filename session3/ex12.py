"""
    Veti primi un input de la tastatura, (numar intreg). Folosind acel input,
    va trebui sa afisati o lista cu toate elementele pana la acel numar, daca
    acel numar este par, altfel, veti afisa o lista cu patratele tuturor
    numerelor pana la acel numar.

    exemplu:
        Veti primi 6, veti afisa [1, 2, 3, 4, 5]
        Veti primi 5, veti afisa [1, 4, 9, 16]
"""

x=input("Introduceti numarul de la tastatura:")
y=int(x)
l=[]
if y%2==0:
    for i in range(0, y):
        l.append(i)
else:
    for i in range(0, y):
        l.append(i**2)

print(l)

#am afisat si 0, sa nu facem discriminari