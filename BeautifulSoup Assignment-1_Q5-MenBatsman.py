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


page5 = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")
page5


# In[5]:


soup5 = BeautifulSoup(page5.content)
soup5


# In[22]:


PlayerName = soup5.find('td',class_="table-body__cell name")
PlayerName.text


# In[23]:


PlayerName1 = []
for i in soup5.find_all('td',class_="table-body__cell name"):
    PlayerName1.append(i.text)


# In[21]:


PlayerName1


# In[24]:


TeamName1 = []
for i in soup5.find_all('td',class_="table-body__cell nationality-logo"):
    TeamName1.append(i.text)


# In[25]:


TeamName1


# In[26]:


Rating1 = []
for i in soup5.find_all('td',class_="table-body__cell u-text-right rating"):
    Rating1.append(i.text)


# In[27]:


Rating1


# In[28]:


print(len(PlayerName1),len(TeamName1),len(Rating1))


# In[37]:


import pandas as pd


# In[38]:


df = pd.DataFrame({'PlayerName':PlayerName1,'TeamName':TeamName1,'Rating':Rating1})


# In[39]:


type(pd)


# In[40]:


df


# In[ ]:




