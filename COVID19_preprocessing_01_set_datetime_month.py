#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
import datetime

#column['확진월'] 추가
df = pd.read_csv('./datasets/COVID19_5.csv', index_col=0)
print(df)


# 확진월 컬럼 추가
df['확진월'] = ''



df['확진일자'][0].split('-')[0] + '-' + df['확진일자'][0].split('-')[1]



# 확진일자를 -로 split하고 앞에 두개 따오기
for i in range(0, len(df)):
    df['확진월'][i] = df['확진일자'][i].split('-')[0] + '-' + df['확진일자'][i].split('-')[1]


print(df.head())



df.to_csv('./datasets/datetime_month_Daejeon_COVID.csv')

# 1월 - 8월만 남기기

df = pd.read_csv('./datasets/datetime_month_Busan_COVID.csv', index_col=0)
print(df.head())

# 10월 제거
df_list = []
for i in range(0, len(df)):
    if df['확진월'][i].split('-')[1] != '10':
        data = df.iloc[i]
        df_list.append(data)

df2 = pd.DataFrame(df_list)
df2.reset_index(drop=True, inplace= True)

df2.head()

# 9월 제거
df2_list = []
for i in range(0, len(df2)):
    if df2['확진월'][i].split('-')[1] != '09':
        data = df2.iloc[i]
        df2_list.append(data)

df3 = pd.DataFrame(df2_list)
df3.reset_index(drop=True, inplace= True)

df3.head()

df3.to_csv('./datasets/datetime_month_Busan_COVID.csv')

df4 = pd.read_csv('./datasets/datetime_month_Busan_COVID.csv', index_col=0)
print(df4.head())