```python
import pandas as pd
df = pd.read_csv("YOUR_DATA.csv",index_col="Your_Index_Col")
#Data Cleaning and correction
df["AAA"] = df["AAA"].fillna("Your_Value")
df["BBB"] = pd.to_numeric(df["BBB"], errors='coerce')
df["CCC"] = df["CCC"].replace({"Wrong_Value":"Correct_Value"})
df["DDD"] = df["DDD"].str.upper()
print("CORRECTED")
print(str.upper("-----Whole Data Base----"))
print("")
print(df)
print("")

#Statistics(mean, sum, max, min)
group = df.groupby("EEE")
print(str.upper("-----mean-----"))
print(group["FFF"].mean(numeric_only=True))
print("\n")

print(str.upper("-----sum-----"))
print(group["GGG"].sum(numeric_only=True))
print("\n")

print(str.upper("-----max-----"))
print(group["HHH"].max(numeric_only=True))
print("\n")

print(str.upper("-----min-----"))
print(group["III"].min(numeric_only=True))
print("\n")

#filter AMOUNT that greater than n and area as YOUR_AREA.
print("XXX area(>5000)")
filtering = df[(df["YYY"]>n) & (df["ZZZ"] == "your_area")]
print(f"\n\n{filtering}")
```
