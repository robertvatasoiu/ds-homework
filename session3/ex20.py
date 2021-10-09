"""
    Veti primi un string de la tastatura.
    Veti primi un numar intreg de la tastatura, x.
    Va trebui sa creati un dictionar care sa contina ca si chei, toate numerele
    pana la x, iar ca si valori caracterele de pe indexurile corespunzatoare.

    Observatii:
        - lungimea stringului va fi mereu egala cu numarul primit
        - indexarea in python incepe de la 0 (prima cheie va fi 0)

    exemplu:
        Veti primi: 'cmi', 3
        Veti printa: {
            0: 'c',
            1: 'm',
            2: 'i'
        }
"""
q=[]
for i in range(0, 2):
    i=input()
    q.append(i)

word=q[0]
number=int(q[1])

d={}
for i in range(0, len(word)):
        d[i]=word[i]

print(d)
