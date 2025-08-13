import pandas as pd
data={
    "name":['nitin','naresh','vikash','suresh'],
    "age":[24,25,14,32],
    "salary":[20000,23000,41000,35000],
    "score":[85,80,41,75]
    
}
df=pd.DataFrame(data)
print(df)
# acess single column
name =df['name']
print(name)
# selecting multiple column
subset =df[['name','salary']]
print(subset)

# filtering single row

high_salary =df[df['salary']>30000]
print(high_salary)

# filtering multiple rows
print("age must be greater than 18 and salary 20k")
filtered= df[(df['age']>18) &(df['salary']>20000)]
print(filtered)
 