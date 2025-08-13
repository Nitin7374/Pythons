import pandas as pd

df =pd.read_csv("Task 5 employee table.csv",encoding="utf-8") 

print("display first 3 rows ")
print(df.head(3))

print("display last 3 rows")
print(df.tail(3))