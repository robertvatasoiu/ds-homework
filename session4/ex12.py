"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""
def dec(func):
    def wraper(*args, **kwargs):
        x=func(*args)
        with open("output12.data", 'w+') as f:
            f.write(str(x))
    return wraper   

@dec
# decorate me
def f(x):
    print(x)


x=f(3)