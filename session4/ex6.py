"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""
def func(s):
    s1=[]
    for i in range(0, len(str(s))):
        x=chr(ord(s[i])+1)
        s1.append(x)
    litere=''.join(s1)
    print(litere)

func('aabbcc')