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


page3 = requests.get("https://www.imdb.com/list/ls009997493")


# In[5]:


page3


# In[6]:


soup3 = BeautifulSoup(page3.content)
soup3


# In[7]:


#For Multiple Names
IndiaName = []
for i in soup3.find_all('h3', class_="lister-item-header"):
    IndiaName.append(i.text)


# In[8]:


IndiaName


# In[11]:


IndiaRating = []
for i in soup3.find_all('div', class_="ipl-rating-star small"):
    IndiaRating.append(i.text)


# In[12]:


IndiaRating


# In[14]:


IndiaYear = []
for i in soup3.find_all('span', class_="lister-item-year text-muted unbold"):
    IndiaYear.append(i.text)


# In[15]:


IndiaYear


# In[16]:


print(len(IndiaName),len(IndiaRating),len(IndiaYear))


# In[17]:


import pandas as pd


# In[18]:


import pandas as pd
df = pd.DataFrame({'Names':IndiaName,'Ratings':IndiaRating,'Years':IndiaYear})


# In[19]:


df


# In[ ]:




