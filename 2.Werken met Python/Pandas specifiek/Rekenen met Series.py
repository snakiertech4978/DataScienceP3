import pandas as pd

series = pd.Series([1, 5, 8, 10, 50])
print((series * 3).to_list())
print(series * 3)
print((series + 10).to_list())
series2 = pd.Series([25, 5, 6, 9, 10, 11])
print((series + series2).to_list())