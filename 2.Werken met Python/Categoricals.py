import pandas as pd
mening = ['niet belangrijk', 'heel belangrijk', 'heel belangrijk', 'een beetje belangrijk', 'heel belangrijk',
          'een beetje belangrijk', 'een beetje belangrijk', 'niet belangrijk', 'heel belangrijk', 'heel belangrijk']
meningMogelijkheden = ['niet belangrijk', 'een beetje belangrijk', 'heel belangrijk', 'extreem belangrijk']
meningIndexen = [0, 2, 2, 1, 2, 1, 1, 0, 2, 2]

meningSeries = pd.Categorical(mening, categories=meningMogelijkheden)
print(meningSeries)
meningSeriesord = pd.Categorical(mening, categories=meningMogelijkheden, ordered =True)
print(meningSeriesord)
print(meningSeries.categories.tolist())
print(meningSeries.codes)