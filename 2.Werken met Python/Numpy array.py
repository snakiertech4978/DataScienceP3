import numpy as np
arr0 = np.zeros(10, dtype=int)
print(arr0)

arr1 = np.ones(5, dtype=int)
print(arr1)

arrr = np.random.randint(6, size=10)
print(arrr)

arrra = np.arange(1.1, 3, 0.3)
print(arrra)
print(type(arrra))
print(type([arrra]))

lijst = [1, 2, 3]
arr = np.array(lijst)
print(arr)
print(type(arr))

arrrandom = np.random.randint(2, size=10)
lijstrand = arrrandom.tolist()
print(lijstrand)
print(type(lijstrand))
