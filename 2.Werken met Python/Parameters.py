def mijn_functie(a, b, c):
    return a + b - c
print(mijn_functie (10, 5, 1))
print(mijn_functie(b=5, a=10, c=1))

"Default waarden"

def verhoog(getal, aantal=1):
    return getal + aantal
print(verhoog(41))
print(verhoog(40, 2))
