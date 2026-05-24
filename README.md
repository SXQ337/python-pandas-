# python-pandas-
This Python script is designed for automated data cleaning and data restructuring. Specifically, it executes data filtering and baseline statistical calculations in one go, while supporting seamless CSV/Excel data import and export capabilities.
``` python
import pandas as pd
df = pd.read_csv("YOUR_DATA.csv",index_col= ["Your_Index_Col"])
df = df.drop_duplicates()
df["AAA"] = df["AAA"].fillna(0)
df["BBB"] = df["BBB"].str.upper()
print(df)
print('')

statistic = df.groupby("CCC")["DDD"].agg(["sum","mean","max","min"])
print(statistic)

filtering = (df["EEE"] == "eee")
filtering1 = (df["FFF"] == "fff")
filtering2 = (df["GGG"] == "ggg")
filtered = df[filtering]
filtered1 = df[filtering1]
filtered2 = df[filtering2]
print(f"\n{filtered}")
print(f"\n{filtered1}")
print(f"\n{filtered2}")

statistic.to_csv("export_data_new_name1.csv")
filtered.to_csv("export_data_new_name2.csv")
filtered1.to_csv("export_data_new_name3.csv")
filtered2.to_csv("export_data_new_name4.csv")
df.to_csv("export_data_new_name5.csv")
```
