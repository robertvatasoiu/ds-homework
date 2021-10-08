"""
    Veti primi un string de la tastatura.
    Va trebui sa printati un tuplu care sa contina toate literele acelui string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: ('c', 'm', 'i')
"""
t=[]
x=input()
for i in x:
    t.append(i)

d=tuple(t)
print(d)