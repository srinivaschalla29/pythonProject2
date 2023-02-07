(import pandas as pd
d1 ={'name':['pankaj','honey','alli'],
     'country':['India','India','usa'],
     'role': ['ceo','cto','cto']}
df1= pd.DataFrame(d1)
print(df1)
df2=pd.DataFrame({'ID':[1,2,3],
                  'name':['prankaj','anupam','amit']})
print(df2)
df_merged = df1.merge(df2,how='right',on=df2['ID'])
print