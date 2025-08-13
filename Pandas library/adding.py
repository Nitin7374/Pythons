import pandas as pd
data={
    "name":['nitin','naresh','vikash','suresh'],
    "age":[24,25,14,32],
    "salary":[20000,23000,41000,35000],
    "score":[85,80,41,75]
    
}
df=pd.DataFrame(data)
print(df)
 
#  adding new column
df["bonus"] = df["salary"] *0.1
print(df)

# entering data into new column
df.insert(0,"Id",[101,102,103,104])
print(df)