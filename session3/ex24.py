"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""
x=input()
number=int(x)
numarvechi=number
invers=0
while number>0:
    rest=number%10
    invers=invers*10 + rest
    number=number//10
    
print(invers)
print(number)
if invers!=numarvechi:
    print('False')
else:
    print('True')

#imi afiseaza doar False
