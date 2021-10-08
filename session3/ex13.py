"""
    Veti primi 2 numere intregi de la tastatura (x si y).
    Va trebui sa le convertiti si apoi sa printati valorea lui x la puterea y.

    exemplu:
        Veti primi: 2 si 3
        Veti printa: 8
"""
l=[]
for i in range (0, 2):
    numbers=int(input())
    l.append(numbers)

power=l[0]**l[1]
print(f"{l[0]} la puterea {l[1]} este: ",power)