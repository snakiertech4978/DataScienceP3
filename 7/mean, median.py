import pandas as pd

x1 = pd.Series([1, 2, 3, 5, 87, 88, 89, 90])
x2 = pd.Series([42, 43, 44, 45, 47, 47, 48, 49])

tabel = pd.DataFrame([[x1.mean(), x2.mean()],
              [x1.median(), x2.median()]],
             index=['mean()', 'median()'], columns=['x1', 'x2'])
print(tabel)