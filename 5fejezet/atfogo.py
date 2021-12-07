import math

def atfogo(b1, b2):
    a = int(b1)
    b = int(b2)
    a *= a
    b *= b
    c = math.sqrt(a+b)
    return c



print(atfogo(2,3)) 