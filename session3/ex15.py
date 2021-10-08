"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""
a=0
x=input()
for i in x:
    if (i=='a') or (i=='e') or (i=='i') or (i=='o') or (i=='u'):
        a+=1


print(a)
