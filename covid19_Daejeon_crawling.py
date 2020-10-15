#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import numpy as np
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from konlpy.tag import Okt


# In[5]:


options = webdriver.ChromeOptions()
#options.add_argument('headless')  # headless를 주면 동작하는 모습을 볼 수 없음
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(3)


# In[6]:


url = 'https://www.daejeon.go.kr/corona19/index.do'


# In[7]:


driver.get(url)


# In[3]:


# 테이블 읽어오기
df = pd.read_html('https://www.daejeon.go.kr/corona19/index.do?menuId=0002')
print(df)


# In[13]:


type(df[0])


# In[15]:


df=pd.DataFrame(df[0])


# In[20]:


df.to_csv('covid19_daejeon.csv')


# In[19]:


covid19_daejon=pd.read_csv('./covid19_daejeon.csv')


# In[18]:


print(covid19_daejon)


# In[ ]:




