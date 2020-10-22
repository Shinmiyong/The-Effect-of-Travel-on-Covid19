#!/usr/bin/env python
# coding: utf-8

# In[74]:


import pandas as pd


# In[75]:


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
import numpy as np
from selenium.webdriver.common.keys import Keys #키워드 검색해야하니까 임포트 해주기 
import re

from konlpy.tag import Okt
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium import webdriver


# In[76]:


options = webdriver.ChromeOptions()
#options.add_argument('headless')  # headless를 주면 동작하는 모습을 볼 수 없음
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(3)


# In[77]:


#경산
dates = []
regions = []

url = 'http://gbgs.go.kr/programs/coronaMove/coronaMove.do'
driver.get(url)

for a in range(2, 665):
    try:
        date = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[{0}]/div[2]/ul/li/a/div/p[5]'.format(a)).text 
        time.sleep(1.0)
        print(date)
        dates.append(date)        
        
                
        region = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[{0}]/div[2]/ul/li/a/div/p[3]'.format(a)).text
        time.sleep(1.0)
        print(region)
        regions.append(region)

    except:
        continue
                
        
driver.close()


# In[78]:


df = pd.DataFrame({ 'date':dates,'region':regions})
df.info()


# In[79]:


df.rename(columns = {"date" : "확진일"}, inplace = True)
df.rename(columns = {"region" : "거주지"}, inplace = True)


# In[80]:


df['지역']='경북 경산'


# In[81]:


df.head()


# In[82]:


df.to_csv('./datasets/gyungsan.csv')


# In[43]:


df = pd.read_csv('./datasets/gunwe01.csv', engine='python', encoding = 'utf-8', index_col=0)       


# In[44]:


for i in range(1,3):
    data = pd.read_csv(
        './datasets/gunwe0{}.csv'.format(i),encoding = 'utf-8',
                index_col=0)
    print(i, data.info())
    df = pd.concat([df, data], ignore_index=True)


# In[45]:


df.info()


# In[70]:


df.head()


# In[48]:


#컬럼 지우기
df.drop_duplicates(inplace=True)


# In[55]:


df[['확진일', '거주지']]


# In[72]:


df


# In[52]:


df.rename(columns = {"date" : "거주지"}, inplace = True)


# In[53]:


df.rename(columns = {"region" : "확진일"}, inplace = True)


# In[71]:


df['지역'] = '경북 영주시'


# In[50]:


df.reset_index(drop=True, inplace=True)


# In[73]:


df.to_csv('./datasets/youngju.covid.csv')

