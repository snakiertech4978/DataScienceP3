import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')

print(df)
print(df.shape)
print(df.info())

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
print(df)
schema_df = pd.read_csv('data/survey_results_schema.csv')
print(schema_df)
print(df.head(10))
print(df.tail(10))
print(df.describe())

