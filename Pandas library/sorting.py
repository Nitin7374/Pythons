import pandas as pd

data ={
    "name" :["nitin","naresh","abhinav","suresh"],
    "age" :[28,45,28,90],
    "salary":[20000,10000,45000,19000]
}
df =pd.DataFrame(data)
print(df)

# sorting by single column
df.sort_values(by="age",ascending=True,inplace=True)
print(df)

# sorting by multiple column
df.sort_values(by=["age","salary"],ascending=[True,True],inplace=True)
print(df)

# ------ Aggrigation --------

avg_sal = df["salary"].mean()
print(avg_sal) 

# group by using single column

group =df.groupby("age")["salary"].sum()
print(group)

# group ny using multiple column

grouped =df.groupby(["age","name"])["salary"].sum()
print(grouped)
