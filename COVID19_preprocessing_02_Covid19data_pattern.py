#!/usr/bin/env python
# coding: utf-8

# # 도

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc


# In[3]:


# 각 지역 코로나 월 별 데이터 불러오기
df = pd.read_csv('./datasets/datetime_month_Gyeonggido_COVID.csv', index_col=0)


# In[4]:


df['카운트'] = 1


# In[5]:


# 8월에 충주시가 몇명인지가 나와야함
grouped = df.groupby(['확진월', '거주지'])
df2 = pd.DataFrame(grouped.count())


# In[6]:


df2.sort_values(by=['확진월'], axis=0, ascending=True, inplace= True)


# In[7]:


df2.reset_index(inplace=True)


# In[8]:


df2.head()


# In[9]:


df2['거주지'].unique()


# In[ ]:





# In[244]:


a_list = []
for i in range(0, len(df2)):
    if df2['거주지'][i] == '연천군':
        data = df2.iloc[i]
        a_list.append(data)


# In[245]:


df3 = pd.DataFrame(a_list)


# In[246]:


df3.reset_index(drop= True, inplace= True)


# In[247]:


# 폰트
font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font_name)


# In[248]:


df3.head()


# In[249]:



# # Basic Bar Chart

# plt.bar(index, tips_sum_by_day)

# plt.title('covid19_monthly_case', fontsize=20)

# plt.xlabel('확진월', fontsize=18)

# plt.ylabel('카운트', fontsize=18)

# plt.xticks(index, label, fontsize=15)

# plt.show()


# In[250]:


plt.figure(figsize=(7,7))
ax = sns.barplot(x = '확진월', y = '카운트', hue= '거주지', data= df3)
#plt.yticks(rotation=270)
plt.show()


# In[251]:


ax.figure.savefig('./pattern/Yeoncheon_pattern.png')


# In[ ]:





# # 특별시, 광역시, 제주

# In[252]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc


# In[269]:


# 각 지역 코로나 월 별 데이터 불러오기
df = pd.read_csv('./datasets/datetime_month_Seoul_COVID.csv', index_col=0)


# In[270]:


df['카운트'] = 1


# In[271]:


grouped = df.groupby(['확진월', '지역'])
df2 = pd.DataFrame(grouped.count())


# In[272]:


df2.sort_values(by=['확진월'], axis=0, ascending=True, inplace= True)


# In[273]:


df2.reset_index(inplace=True)


# In[274]:


df2.head()


# In[278]:


plt.figure(figsize=(7,7))
ax = sns.barplot(x = '확진월', y = '카운트', hue= '지역', data= df2)
plt.yticks(rotation=270)


# In[276]:


ax.figure.savefig('./pattern/Seoul_pattern.png')


# # 그래프로 나타내기 -2

# In[281]:


#data 부르기
cases = pd.read_csv('./datasets/datetime_month_Seoul_COVID.csv', index_col=0)

cases.shape
cases.head()


# In[290]:


cases['카운트'] = 1
cases.head()


# In[294]:


cases['카운트'] = df['카운트'].astype(float)


# In[295]:


cases_sum_by_month = cases.groupby('확진월').카운트.sum()

cases_sum_by_month


# In[297]:


label = ['2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08']

index = np.arange(len(label))


# In[292]:


# Basic Bar Chart

plt.bar(index, cases_sum_by_month)

plt.title('covid19_monthly_case', fontsize=20)

plt.xlabel('확진월', fontsize=15)

plt.ylabel('카운트', fontsize=15)

plt.xticks(index, label, fontsize=15)

plt.show()


# In[ ]:




