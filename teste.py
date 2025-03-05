import pandas as pd 

df = pd.read_parquet('data/output/reddit_20250305.parquet')

print(df.head())