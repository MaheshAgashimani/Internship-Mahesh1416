#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page5 = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
page5


# In[5]:


soup5 = BeautifulSoup(page5.content)
soup5


# In[6]:


PlayerName1 = []
for i in soup5.find_all('td',class_="table-body__cell name"):
    PlayerName1.append(i.text)


# In[7]:


PlayerName1


# In[8]:


TeamName1 = []
for i in soup5.find_all('td',class_="table-body__cell nationality-logo"):
    TeamName1.append(i.text)


# In[9]:


TeamName1


# In[10]:


Rating1 = []
for i in soup5.find_all('td',class_="table-body__cell u-text-right rating"):
    Rating1.append(i.text)


# In[11]:


Rating1


# In[12]:


print(len(PlayerName1),len(TeamName1),len(Rating1))


# In[13]:


import pandas as pd


# In[14]:


df = pd.DataFrame({'PlayerName':PlayerName1,'TeamName':TeamName1,'Rating':Rating1})


# In[15]:


df


# In[ ]:




