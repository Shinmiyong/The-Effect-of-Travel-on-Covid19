#!/usr/bin/env python
# coding: utf-8

# In[161]:


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


# In[162]:


options = webdriver.ChromeOptions()
#options.add_argument('headless')  # headless를 주면 동작하는 모습을 볼 수 없음
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(3)


# In[ ]:


#인천 크롤링


# In[163]:


incheons = []
url = 'https://www.incheon.go.kr/health/HE020409'
driver.get(url)
for a in range(2, 957):
    incheon = driver.find_element_by_xpath(
            '//*[@id="content"]/div[3]/div/div/div/section/div[3]/div[{0}]/div[1]/a'.format(a)).text #호텔이름 xpath 
    time.sleep(0.5)
    print(incheon)
    incheons.append(incheon)
    
driver.close()


# In[164]:


df = pd.DataFrame({'incheon':incheons})
df.head()
df.info()


# In[165]:


df.to_csv('./datasets/incheon_covid.csv') 


# In[167]:


df = pd.read_csv('./datasets/incheon_covid.csv', encoding = 'utf-8', index_col=0)              


# In[168]:


df['확진일'] = df.incheon.str.split('(').str[1]
print(df.head())


# In[169]:


#split 해서 새로운 칼람 만들기 
df['거주지'] = df.incheon.str.split('(').str[0]
print(df.head())


# In[170]:



del df['incheon']
df.head()


# In[171]:


df.to_csv('./datasets/incheon_covid19.csv') 


# In[199]:


df = pd.read_csv('./datasets/incheon_covid19.csv', encoding = 'utf-8', index_col=0)  


# In[200]:


df.head()


# In[201]:


con=[]
for i in range(len(df['확진일'])):
    con.append(df['확진일'][i].split('/')[0])
df['확진일자']=con


# In[203]:


on=[]
for i in range(len(df['거주지'])):
    on.append(df['거주지'][i].split('#')[1])
df['거주장소']=on


# In[204]:


df


# In[205]:


df


# In[217]:


#컬럼 지우기
del df['거주지']
df


# In[218]:


df.rename(columns = {"거주장소" : "거주지"}, inplace = True)


# In[219]:


df


# In[215]:


on=[]
for i in range(len(df['거주지'])):
    on.append(df['거주지'][i].split(' ')[1])
df['거주장소']=on


# In[216]:


df


# In[220]:


df.info()


# In[222]:


df.to_csv('./datasets/incheon_covid.csv') 

