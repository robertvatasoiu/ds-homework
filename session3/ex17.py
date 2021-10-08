"""
    Veti primi un string de la tastatura.
    Veti primi un intreg de la tastatura, x.
    Va trebui sa printati acel string, concatenat de x ori.

    exemplu:
        Veti primi: 'cmi', 5
        Veti printa: 'cmicmicmicmicmi'
"""


inputs=[]
for i in range(0,2):
    inputs.append(input())


x=inputs[0] * int(inputs[1])
print(x)

