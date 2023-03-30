import pandas as pd
ist = [{'a':1, 'b':2, 'c':3},
       {'a':74, 'b':75, 'c':76}]
df = pd.DataFrame(ist)
print(df)
list = df.values
print(list.tolist())
df = df.drop(df.index[0])
print(df)
