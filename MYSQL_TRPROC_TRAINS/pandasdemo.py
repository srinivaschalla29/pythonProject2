import pandas as pd
d={'Team':["India","austrlia","pakistan","Srilanka","england"],
'rank':[1,2,3,4,5],
'winper':['60%','55%','45%','35%','48%']
}
df=pd.DataFrame(d)
df.rename(columns={"Rank":"Ranking"},inplace=True)
print(df.iloc[:3,-1])