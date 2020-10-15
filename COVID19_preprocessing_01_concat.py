#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime


# In[3]:


df = pd.read_csv('./datasets/COVID19_1.csv', index_col=0)
print(df)


# In[300]:


df2 = pd.read_csv('./datasets/COVID19_5.csv', index_col=0)
print(df2)


# In[311]:


df = pd.read_csv('./datasets/COVID19_1.csv')
for i in range(2,4):
    data = pd.read_csv('./datasets/COVID19_{}.csv'.format(i))
    df = pd.concat([df, data], ignore_index=True)
df.drop(['Unnamed: 0'], axis=1, inplace=True)
print(df.loc[4500:5000])


# In[312]:


print(df.info())


# In[313]:


df.to_csv('./datasets/COVID19_capital.csv')


# In[314]:


df = pd.read_csv('./datasets/COVID19_capital.csv', index_col = 0)

print(df.info())


# In[ ]:




