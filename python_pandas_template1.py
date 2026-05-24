```python
#immense big data handling up to >10000 columns
import pandas as pd
import numpy as np
df = pd.read_csv("Your_Data.csv",index_col="Your_Index_Col")
print(df)
print('')

df["AAA"] = "aaa"
df.loc[(df["BBB"] >= n)&(df["CCC"] == "ccc"),"col_N+1"] = "VALUE_OR_NUM" #chain condition from col A···col N to affect col N+1
print(str.upper("------YOUR_ARRANGEMENT_NAME------"))
print('')
print(df)
print('')

filtering1 = (df["DDD"] == "VALUE_OR_NUM")
TARGET_FILTER = df[filtering1]
NONE_TARGET_FILTER = df[~filtering1]
print(TARGET_FILTER)
print(NONE_TARGET_FILTER)

#new:sort values
df_sort = df.sort_values("Claim_Amount",ascending = False)
print(str.upper("----Sort----"))
print(df_sort)

#export csv
df.to_csv("YOUR_DATA_NAME(NEW).csv")


#Another template combined with numpy basics. (USE YOUR THE VALUE AS YOU WANT)

#csv practice 
import pandas as pd
import numpy as np
df = pd.read_csv("csv_practice2.csv",index_col="Policy ID")

risk_score = (df["BMI"]*0.5)
df["Risk_Score"] = np.nan
print(str.upper("------final risk report------"))
print(f"\n{df}")

df.loc[df["Smoking Status"] == "Yes","Risk_Score"] = risk_score + 10
df.loc[df["Smoking Status"] != "Yes","Risk_Score"] = 0
print('')
print(str.upper("-----Risk score-----"))
print(f"\n{df.to_string()}")

filtering1 = (df["BMI"]<=18.00)
bmi_low = df[filtering1]
bmi_high = df[~filtering1]
print(f"\nLOW RISK:")
print(bmi_low)
print(f"\nHIGH RISK:")
print(bmi_high)

filtering2 = (df["Risk_Score"] != float(0)) & (df["BMI"]>18.00) & (df["Income"] < 3000)
final = df[filtering2]
print(f"\n{"-----Final High Risk-----".upper()}")
print(f"\n{final}")
final.to_csv("Final High Risk.csv")
```
