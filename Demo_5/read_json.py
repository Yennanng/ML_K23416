import pandas as pd
df=pd.read_json("../dataset/SaleTransactions/SalesTransactions.json", encoding="utf-8",dtype="unicode")
print(df)