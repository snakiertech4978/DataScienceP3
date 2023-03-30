import pandas as pd
series = pd.Series(range(1, 10))
print(series)

print(series[0:8:2])

select = [0, 2, 1]
print(series[select])
print(series > 4)
print(series[series > 4])
even = ((series % 2)==0)
print(series[even])

vakken = pd.Series(['data science', 'programmeren', 'databanken', 'hardware', 'operating systems'])
scores = pd.Series([18, 15, 13, 16, 12])
print(vakken[scores > 15])

