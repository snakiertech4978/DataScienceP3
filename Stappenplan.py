"1. Bestand beijken"


"seperator?"
"decimal?"
"commentaar skip?"
"header?"
"encodering?"
"Woorden gebruikt om ontbrekende voorwaarden voor te stellen?"

"2. Invullen ->"
data = pd.read_csv('bestandsnaam.csv', sep='', decimal='', skip=aantalComentaarRegels, header=regelnummer, encoding='', na_values=[])

"3. Data chekken"
print(data.info())
print(data.head())
print(data.describe())

"4. Datatypes juist zetten"
"strings -> gehele getallen: " to_numeric()
"strings -> kommagetallen" to_numeric()
"strings" unique(), Categorical
"verkeerde waarden:" replace()

"5. Ontbrekende waarden"
"Aantal ontbrekende waarde" data.isna().sum().sum()

'rijen ontbrekende waarden weergeven'
rowsWithNan = data[data.isna().any(axis =1)]
print(rownsWithNan)
'kolommen ontbrekende waarden'
columsWithNn = data[data.isna().any(axis =0)]
print(rowsWithNan)