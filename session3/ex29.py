"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""

s=input()
vocale=0
consoane=0
for i in s:
    if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
        vocale+=1
    else:
        consoane+=1

print(f"Avem {vocale} vocale si {consoane} consoane")

