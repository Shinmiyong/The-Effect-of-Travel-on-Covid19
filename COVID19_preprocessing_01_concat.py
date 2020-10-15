import pandas as pd
import datetime


df = pd.read_csv('./datasets/COVID19_1.csv', index_col=0)
print(df)

df2 = pd.read_csv('./datasets/COVID19_5.csv', index_col=0)
print(df2)

df2['지역'] = '인천'

df2.to_csv('./datasets/COVID19_2.csv')

df3=pd.read_csv('./datasets/COVID19_2.csv', index_col=0)
print(df3)

for i in range(0, len(df2)):
    if len(df2.iloc[i]['확진일']):
        df2.iloc[i]['확진일'] = df2.iloc[i]['확진일'].replace('2020.','')
print(df2[350:450])

df2.to_csv('./datasets/COVID19_2.csv')

df = pd.read_csv('./datasets/COVID19_1.csv')
for i in range(2,4):
    data = pd.read_csv('./datasets/COVID19_{}.csv'.format(i))
    df = pd.concat([df, data], ignore_index=True)
df.drop(['Unnamed: 0'], axis=1, inplace=True)
print(df.loc[4500:5000])

print(df.info())


df.to_csv('./datasets/COVID19_capital.csv')


df = pd.read_csv('./datasets/COVID19_capital.csv', index_col = 0)

print(df.info())






