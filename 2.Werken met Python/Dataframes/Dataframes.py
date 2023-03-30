import pandas as pd
import numpy as np

x = pd.Series(range(1,6))
y = ["foo", "bar", "bla", "boe", "foo"]
z = np.random.randint(10, size=5)
f = pd.DataFrame({'id':x, 'naam':y, 'score':z})
print(f)

"Lezen + manipuleren"

print(len(f))
print(f.columns.size)
print(f.columns.tolist())
print(f.index.tolist())

"Kolommen"
print(f['id'])
print(f.naam)
print(f.id)

print(type(f.naam))
"kolommen verwijderen"
f = f.drop(columns='id')
print(f)

f.drop(columns='score', inplace=True)
print(f)

"kolom toevoegen"
f['score'] = np.random.randint(10, size=5)
f['key'] = [10, 20, 30, 60, 40]
print(f)

"selecteren + verwijderen rijen"

print(f.loc[1])
print(f.loc[1:3])
f = f.drop(1)
print(f)

"Rij- en kolomnummers"
print(f.iloc[3, 2])
print(f.iloc[3])
print(f.iloc[1:4])
print(f.iloc[:, 0])
print(f.iloc[:, 1:3])
print(f.iloc[0:2, 1:3])

