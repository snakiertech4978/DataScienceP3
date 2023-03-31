import pandas as pd
import numpy as np
lijst = [1, 2, 3]
array = np.array(lijst)
print(array)
print(type(array))

arr = np.random.randint(6, size=10)
lijst = arr.tolist()
print(lijst)
print(type(lijst))

series = pd.Series([1,
                    5, 8, 10, 50])
print((series * 3).to_list())
print(series * 3)
print((series + 10).to_list())
series2 = pd.Series([25, 5, 6, 9, 10, 11])
print((series + series2).to_list())
