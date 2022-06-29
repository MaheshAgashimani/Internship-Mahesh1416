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


page4 = requests.get("https://presidentofindia.nic.in/former-presidents.htm")


# In[7]:


page4


# In[8]:


soup4 = BeautifulSoup(page4.content)
soup4


# In[ ]:




