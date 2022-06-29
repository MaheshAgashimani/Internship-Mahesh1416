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


page5 = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")


# In[5]:


page5


# In[6]:


soup5 = BeautifulSoup(page5.content)
soup5


# In[13]:


first_data=soup5.find("div",class_="rankings-block__top-player")


# In[15]:


TeamName = []
for i in soup5.find_all('span',class_="u-hide-phablet"):
    TeamName.append(i.text)


# In[16]:


TeamName


# In[17]:


Matches = []
for i in soup5.find_all('td',class_="table-body__cell u-center-text"):
    Matches.append(i.text)


# In[18]:


Matches


# In[19]:


Rating = []
for i in soup5.find_all('td',class_="table-body__cell u-text-right rating"):
    Rating.append(i.text)


# In[20]:


Rating


# In[21]:


print (len(TeamName),len(Matches),len(Rating))


# In[ ]:




