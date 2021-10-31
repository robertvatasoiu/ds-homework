"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""


def dec(func):
    def wraper():
        y = []
        x = func()
        for i in range(0, len(str(x))):
            s = x[i].upper()
            y.append(s)
        newstring = "".join(y)
        print(newstring)

    return wraper


@dec
# decoarate me
def f():
    return "cmi"


f()
