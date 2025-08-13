import pandas as pd

data = {
    "name" :['nitin', 'shyam','ram'],
    "age" :[23,16,51],
    "city" :['jaipur','sikar','churu']
}

df = pd.DataFrame(data)
print(df)

# save
df.to_csv("output.csv",index=False)
df.to_json("output.json",index=False)

