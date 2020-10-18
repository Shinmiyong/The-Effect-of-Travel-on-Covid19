#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime


# # 경기도

# In[3]:


gg = pd.read_csv('./datasets/COVID19_gg.csv', index_col=0)
gg.head()


# In[4]:


gg2=[]
for i in range(len(gg['확진일'])):
    gg2.append('2020.' + gg['확진일'][i])
gg['확진일자']=gg2
print(gg)


# In[5]:


del gg['확진일']
print(gg)


# In[8]:


gg[gg['확진일자']=='2020.8.2019']


# In[9]:


gg.loc[2328] =['수원시','경기','2020.8.20']
print(gg.loc[2328])


# In[11]:


for i in range(0, len(gg)):
    if len(gg.iloc[i]['확진일자']) > 5:
        gg.iloc[i]['확진일자'] = gg.iloc[i]['확진일자'].split('/')[0]
print(gg)


# In[12]:


gg['확진일자'] = pd.to_datetime(gg['확진일자'])


# In[14]:


gg.to_csv('./datasets/COVID19_Gyeonggido.csv')


# # 인천

# In[21]:


ic = pd.read_csv('./datasets/COVID19_incheon.csv', index_col=0)
ic.head()


# In[22]:


for i in range(0, len(ic)):
    if len(ic.iloc[i]['확진일']):
        ic.iloc[i]['확진일'] = ic.iloc[i]['확진일'].replace('2020.','')
print(ic[350:450])


# In[23]:


ic2=[]
for i in range(len(ic['확진일'])):
    ic2.append('2020.' + ic['확진일'][i])
ic['확진일자']=ic2
print(ic)


# In[24]:


del ic['확진일']


# In[28]:


for i in range(0, len(ic)):
    if len(ic.iloc[i]['확진일자']):
        ic['확진일자'][i] = ic.iloc[i]['확진일자'].replace('202.','')


# In[31]:


ic['확진일자'] = pd.to_datetime(ic['확진일자'])
ic.head()


# In[32]:


ic.to_csv('./datasets/COVID19_Incheon.csv')


# # 서울

# In[33]:


sc = pd.read_csv('./datasets/COVID19_seoul.csv', index_col=0)
sc.head()


# In[34]:


sc2=[]
for i in range(len(sc['확진일'])):
    sc2.append('2020.' + sc['확진일'][i])
sc['확진일자']=sc2
print(sc)


# In[35]:


del sc['확진일']


# In[37]:


sc['확진일자'] = pd.to_datetime(sc['확진일자'])
sc.head()


# In[38]:


sc.to_csv('./datasets/COVID19_Seoul.csv')

