"""
    Veti primi un string de la tastatura.
    Veti primi doua numere intregi de la tastatura, x, y.
    Va trebui sa printati substringul de la indexul x la indexul y (inclusiv).

    exemplu:
        Veti primi: 'Center for Intelligent Machines', 2, 5
        Veti printa: 'nter'
"""

inputs=[]

for i in range(0,3):
    inputs.append(input())

print(inputs)
x=inputs[0]
y=int(inputs[1])
z=int(inputs[2])
print(x[y:z+1])


