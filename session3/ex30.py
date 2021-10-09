"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""
s=input()
rotundaD=0
rotundaI=0
patrataI=0
patrataD=0
acoladaI=0
acoladaD=0
for i in s:
    if i=='(':
        rotundaD+=1
    elif i==')':
        rotundaI+=1
    elif i=='[':
        patrataD+=1
    elif i==']':
        patrataI+=1
    elif i=='{':
        acoladaD+=1
    elif i=='}':
        acoladaI+=1

if rotundaD==rotundaI and acoladaI==acoladaD and patrataI==patrataD:
    print("True")
else:
    print("False")



