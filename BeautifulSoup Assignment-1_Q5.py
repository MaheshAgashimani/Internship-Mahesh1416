#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')


# In[3]:


get_ipython().system('pip install requests')


# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


page5 = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")


# In[6]:


page5


# In[7]:


soup5 = BeautifulSoup(page5.content)
soup5


# In[19]:


Team = soup5.find('span',class_="u-hide-phablet")
Team.text


# In[20]:


Matches = soup5.find('td',class_="table-body__cell u-center-text")
Matches.text


# In[23]:


Rating = soup5.find('td',class_="table-body__cell u-text-right rating")
Rating.text


# In[22]:


Team1 = soup5.find('td',class_="rankings-block__banner--team-name")
Team1.text


# In[24]:


Points = soup5.find('td',class_="rankings-block__banner--points")
Points.text


# In[25]:


TeamName = []
for i in soup5.find_all('span',class_="u-hide-phablet"):
    TeamName.append(i.text)


# In[29]:


TeamName


# In[40]:


Matches = []
for i in soup5.find_all('td',class_="table-body__cell u-center-text"):
    Matches.append(i.text)


# In[41]:


Matches


# In[36]:


Rating1 = []
for i in soup5.find_all('td',class_="table-body__cell u-text-right rating"):
    Rating1.append(i.text)


# In[37]:


Rating1


# In[42]:


print (len(TeamName),len(Matches),len(Rating1))


# In[ ]:




