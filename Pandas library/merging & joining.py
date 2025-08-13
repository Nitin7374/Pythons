# merging

import pandas as pd

df_customer = pd.DataFrame({
    "customer_id":[1,2,3,4],
    "cust_name":["nitin","suresh","anu","nik"]

})

df_order= pd.DataFrame({
    "customer_id":[1,3,4,5],
    "amount":[154,756,157,000]
})

mergeing= pd.merge(df_customer,df_order,on="customer_id",how="inner")
print(mergeing)