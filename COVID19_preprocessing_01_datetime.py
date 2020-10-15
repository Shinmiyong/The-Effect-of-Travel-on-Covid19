#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import datetime


# In[38]:


df = pd.read_csv('./datasets/COVID19_Busan.csv', index_col=0)
print(df)


# In[63]:


for i in range(0, len(df)):
    if len(df.iloc[i]['확진일자']):
        df.iloc[i]['확진일자'] = df.iloc[i]['확진일자'].replace(' ','')
print(df)


# In[64]:


df['확진일자'] = pd.to_datetime(df['확진일자'])


# In[65]:


print(df.head(10))


# In[66]:


df.to_csv('./datasets/COVID19_4.csv')


# In[3]:


df2 = pd.read_csv('./datasets/COVID19_sejong.csv', index_col=0)
print(df2)


# In[5]:


df2 = df2[['거주지', '지역', '확진일자']]
print(df2)


# In[6]:


for i in range(0, len(df2)):
    if len(df2.iloc[i]['확진일자']):
        df2['확진일자'][i] = df2.iloc[i]['확진일자'].replace(' ','')
print(df2)


# In[7]:


df2['확진일자'] = pd.to_datetime(df2['확진일자'])


# In[9]:


df2.to_csv('./datasets/COVID19_3.csv')


# In[16]:


df3 = pd.read_csv('./datasets/COVID19_jeonnam.csv', index_col=0)
print(df3)


# In[17]:


df4=[]
for i in range(len(df3['확진일'])):
    df4.append('2020.' + df3['확진일'][i])
df3['확진일자']=df4
print(df3)


# In[18]:


del df3['확진일']
print(df3)


# In[27]:


for i in range(0, len(df3)):
    if len(df3.iloc[i]['확진일자']):
        df3['확진일자'][i] = df3.iloc[i]['확진일자'].replace('월 ','.').replace('일','')
print(df3[90:98])


# In[33]:


df3[df3['확진일자']=='2020.7월26']


# In[34]:


df3.loc[139] =['순천시','전남','2020.7.26']
print(df3.loc[139])


# In[36]:


df3['확진일자'] = pd.to_datetime(df3['확진일자'])


# In[37]:


df3.to_csv('./datasets/COVID19_4.csv')


# In[ ]:




