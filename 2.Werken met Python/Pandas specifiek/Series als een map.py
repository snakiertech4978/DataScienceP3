import pandas as pd

series = pd.Series([10, 20, 30, 40, 50], index=[4, 3, 8, 6, 10])
print(series)
series[100] = 5
series['hello'] = 42
print(series)
print(series[3])
print(series['hello'])