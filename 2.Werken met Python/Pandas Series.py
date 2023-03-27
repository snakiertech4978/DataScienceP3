import pandas as pd
"Aan de hand van een lijst kan een pandas series gemaakt worden"
lijst = [10, 20, 30, 40, 50, 60]
series = pd.Series(lijst)
print(series)
"Series terugzetten naar een list"
print(series.tolist())
"_______________________________________________________________________________________________________________________" \
"Rekenen met Series"
series = pd.Series([2, 2, 0, 5, 1, 4, 4, 0, 0, 3])
print(series.tolist)
"Vermenigvuldigen = vermenigvuldigt met de getallen, list om plek te besparen"
print(((series) * 3).tolist)
