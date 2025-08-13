import pandas as pd
data={
    "name":['nitin','naresh','vikash','suresh'],
    "age":[24,25,14,32],
    "salary":[20000,23000,41000,35000],
    "score":[85,80,41,75]
    
}
df=pd.DataFrame(data)
print(df)

# remove column from table
df.drop(columns=["score"],inplace=True)
print(df)