#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install bs4')


# In[5]:


get_ipython().system('pip install requests')


# In[6]:


from bs4 import BeautifulSoup
import requests


# In[7]:


page1 = requests.get("https://www.wikipedia.org")


# In[8]:


page1


# In[9]:


soup1 = BeautifulSoup(page1.content)
soup1


# In[18]:


Header = soup1.find('div',class_="central-featured-lang lang1")
Header


# In[19]:


Header.text


# In[20]:


Header.text.split()


# In[21]:


Header.text.split()[0]


# In[28]:


Header1 = []

for i in soup1.find_all('div',class_="central-featured"):
    Header1.append(i.text)


# In[29]:


Header1


# In[30]:


Header1.text


# In[ ]:





# In[ ]:




