#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[6]:


r1 = requests.get("https://www.cnbc.com/world/?region=world")
coverpage = r1.content


# In[7]:


soup6 = BeautifulSoup(coverpage, 'html5lib')


# In[14]:


coverpage_news = soup6.find_all('h2', class_='LatestNews-headline')


# In[16]:


coverpage_news.text


# In[ ]:





# In[ ]:




