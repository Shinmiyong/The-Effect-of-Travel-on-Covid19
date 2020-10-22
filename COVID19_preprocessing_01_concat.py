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

print(type(df.확진일[0]))

'2020.' + df.확진일[0]

df2=[]
for i in range(len(df['확진일'])):
    df2.append('2020.' + df['확진일'][i])
df['확진일자']=df2
print(df)

del df['확진일']
print(df)

df[df['확진일자']=='2020.8.2019']

df.loc[2328] =['수원시','경기','2020.8.20']
print(df.loc[2328])

df[df['확진일자']=='2020.4.13/5.15']

for i in range(0, len(df)):
    if len(df.iloc[i]['확진일자']) > 5:
        df.iloc[i]['확진일자'] = df.iloc[i]['확진일자'].split('/')[0]
print(df)

for i in range(0, len(df)):
    if len(df.iloc[i]['확진일자']):
        df.iloc[i]['확진일자'] = df.iloc[i]['확진일자'].replace('202.','')

df['확진일자'] = pd.to_datetime(df['확진일자']) #기존의 Date컬럼이 덮어씌어짐

print(df.head(10))

df.to_csv('./datasets/COVID19_capital.csv')