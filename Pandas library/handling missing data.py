import pandas as pd
data={
    "name":['nitin',None,'vikash','suresh'],
    "age":[24,None,14,32],
    "salary":[20000,None,41000,35000],
    "score":[85,None,41,75]
    
}
df=pd.DataFrame(data)
print(df)

# finding missing value
print(df.isnull())
# no of missing value
print(df.isnull().sum())




# -----------Handling the missing value -------------

# delete the none value row
# df.dropna(inplace=True)
# print(df)

# replacing 0 value in the place of none value
# df.fillna(0,inplace=True)
print(df)

# replacing some value in the place of none 
# for age
df["age"].fillna(df["age"].mean(),inplace=True)
print(df)

# for salary
df["salary"].fillna(df["salary"].mean(),inplace=True)
print(df)

# for score
df["score"].fillna(df["score"].mean(),inplace=True)
print(df)

# for name
df.loc[1,"name"] ="Naresh"
print(df)
