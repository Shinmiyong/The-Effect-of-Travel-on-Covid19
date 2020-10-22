
import pandas as pd
import numpy as np
import datetime



df = pd.read_csv('./datasets/COVID19_Busan.csv', index_col=0)
print(df)


for i in range(0, len(df)):
    if len(df.iloc[i]['확진일자']):
        df.iloc[i]['확진일자'] = df.iloc[i]['확진일자'].replace(' ','')
print(df)


df['확진일자'] = pd.to_datetime(df['확진일자'])


print(df.head())


df.to_csv('./datasets/COVID19_2.csv')


df2 = pd.read_csv('./datasets/COVID19_sejong.csv', index_col=0)
print(df2)


df2 = df2[['거주지', '지역', '확진일자']]
print(df2)


for i in range(0, len(df2)):
    if len(df2.iloc[i]['확진일자']):
        df2['확진일자'][i] = df2.iloc[i]['확진일자'].replace(' ','')
print(df2)


df2['확진일자'] = pd.to_datetime(df2['확진일자'])



df2.to_csv('./datasets/COVID19_3.csv')



df3 = pd.read_csv('./datasets/COVID19_jeonnam.csv', index_col=0)
print(df3)


df4=[]
for i in range(len(df3['확진일'])):
    df4.append('2020.' + df3['확진일'][i])
df3['확진일자']=df4
print(df3)


del df3['확진일']
print(df3)



for i in range(0, len(df3)):
    if len(df3.iloc[i]['확진일자']):
        df3['확진일자'][i] = df3.iloc[i]['확진일자'].replace('월 ','.').replace('일','')
print(df3[90:98])


df3[df3['확진일자']=='2020.7월26']



df3.loc[139] =['순천시','전남','2020.7.26']
print(df3.loc[139])


df3['확진일자'] = pd.to_datetime(df3['확진일자'])


df3.to_csv('./datasets/COVID19_4.csv')

df4 = pd.read_csv('./datasets/COVID19_Daejeon.csv', index_col=0)
print(df4.head())

df4.info()

df4 = df4[['거주지', '지역', '확진일자']]
print(df)

#colum명 변경
df4.rename(columns = {'확진일자' : '확진일'}, inplace = True)
print(df.head())

#부동소수형(float64)를 문자열(string)로 변환
df4_list = []
for i in range(len(df4['확진일'])):
    df4_list.append(str(df4['확진일'][i]))

df4['확진일'] = df4_list
type(df4['확진일'])

df5=[]
for i in range(len(df4['확진일'])):
    df5.append('2020.' + df4['확진일'][i])
df4['확진일자']=df5
print(df4)

#coiumn['확진일'] 삭제
del df4['확진일']
print(df4)

df4['확진일자'] = pd.to_datetime(df4['확진일자'])
df.to_csv('./datasets/COVID19_5.csv')

df6 = pd.read_csv('./datasets/COVID19_seoul.csv', index_col=0)
print(df6.head())

df7=[]
for i in range(len(df6['확진일'])):
    df7.append('2020.' + df6['확진일'][i])
df6['확진일자']=df7
print(df6)

del df6['확진일']
print(df6)

df6['확진일자'] = pd.to_datetime(df6['확진일자'])
df.to_csv('./datasets/COVID19_1.csv')