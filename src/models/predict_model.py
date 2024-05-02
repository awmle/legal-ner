import pandas as pd


df = pd.read_csv('./data/raw/wine_quality.csv')

for col in df.columns:
    print(f"{col} - {df[col].min()} | {df[col].max()}")