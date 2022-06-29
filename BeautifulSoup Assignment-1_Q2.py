#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install requests')


# In[4]:


from bs4 import BeautifulSoup
import requests


# In[9]:


page2 = requests.get("https://www.imdb.com/search/title/?groups=top_100")


# In[11]:


page2


# In[12]:


soup2 = BeautifulSoup(page2.content)
soup2


# In[15]:


Name = soup2.find('h3', class_="lister-item-header")
Name


# 

# In[41]:


#For Multiple Names
Name = []
for i in soup2.find_all('h3', class_="lister-item-header"):
    Name.append(i.text)


# In[19]:


#For Multiple Names
Rating = []
for i in soup2.find_all('div', class_="ratings-bar"):
    Rating.append(i.text)


# In[32]:


Rating


# In[33]:


Year = []
for i in soup2.find_all('span', class_="lister-item-year text-muted unbold"):
    Year.append(i.text)


# In[34]:


Year


# In[35]:


print(len(Name),len(Rating),len(Year))


# In[36]:


import pandas as pd


# In[39]:


import pandas as pd
df = pd.DataFrame({'Names':Name,'Ratings':Rating,'Years':Year})


# In[40]:


df


# In[ ]:




