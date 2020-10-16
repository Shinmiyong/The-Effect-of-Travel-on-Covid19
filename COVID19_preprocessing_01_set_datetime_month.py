#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
import datetime


# In[121]:


df = pd.read_csv('./datasets/COVID19_5.csv', index_col=0)
print(df)


# In[122]:


# 확진월 컬럼 추가
df['확진월'] = ''


# In[123]:


df['확진일자'][0].split('-')[0] + '-' + df['확진일자'][0].split('-')[1]


# In[124]:


# 확진일자를 -로 split하고 앞에 두개 따오기
for i in range(0, len(df)):
    df['확진월'][i] = df['확진일자'][i].split('-')[0] + '-' + df['확진일자'][i].split('-')[1]


# In[125]:


print(df.head())


# In[126]:


df.to_csv('./datasets/datetime_month_Daejeon_COVID.csv')


# In[ ]:




