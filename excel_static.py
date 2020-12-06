import pandas as pd

df=pd.read_excel("data.xlsx",sheet_name='11월판매데이터')
#print(df)

grouped=df.groupby(by=['품번'],as_index=False).sum()
grouped.to_excel('text.xlsx',sheet_name='test1')
print(grouped)