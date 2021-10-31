"""
    Ex. 11: Scrieti un decorator care sa logheze outputul unei functii
    pe care o decoreaza, intr-un fisier "output11.data".

    https://www.w3schools.com/python/python_file_write.asp

    Functia decorata este f.
"""


def dec(func):
    def wraper():
        x = func()
        with open("output11.data", "w+") as f:
            f.write(x)

    return wraper


@dec
# decorate me
def f():
    return "CMI"


f()
