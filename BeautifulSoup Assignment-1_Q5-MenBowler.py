#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[9]:


page5 = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page5


# In[10]:


soup5 = BeautifulSoup(page5.content)
soup5


# In[11]:


PlayerName1 = []
for i in soup5.find_all('td',class_="table-body__cell rankings-table__name name"):
    PlayerName1.append(i.text)


# In[12]:


PlayerName1


# In[13]:


TeamName1 = []
for i in soup5.find_all('td',class_="table-body__cell nationality-logo rankings-table__team"):
    TeamName1.append(i.text)


# In[14]:


TeamName1


# In[15]:


Rating1 = []
for i in soup5.find_all('td',class_="table-body__cell rating"):
    Rating1.append(i.text)


# In[16]:


Rating1


# In[17]:


print(len(PlayerName1),len(TeamName1),len(Rating1))


# In[18]:


import pandas as pd
df = pd.DataFrame({'PlayerName':PlayerName1,'TeamName':TeamName1,'Rating':Rating1})


# In[19]:


df


# In[ ]:




