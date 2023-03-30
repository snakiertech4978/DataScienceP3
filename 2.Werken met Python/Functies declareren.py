import numpy as np
import math
def mijn_functie(n):
    result = math.sqrt(n) / 2
    return result
print(mijn_functie(9))

def mimax(x):
    return[np.min(x), np.max(x)]
mi, ma = mimax(range(1,6))
print(mi)
print(ma)
