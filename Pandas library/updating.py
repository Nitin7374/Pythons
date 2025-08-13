import pandas as pd
data={
    "name":['nitin','naresh','vikash','suresh'],
    "age":[24,25,14,32],
    "salary":[20000,23000,41000,35000],
    "score":[85,80,41,75]
    
}
df=pd.DataFrame(data)
print(df)

# updating values
df.loc[1,"name"] ="hitesh"
print(df)

# updating multiple values
df["salary"] =df["salary"] *1.05
print(df)