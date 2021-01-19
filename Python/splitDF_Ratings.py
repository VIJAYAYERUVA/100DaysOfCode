#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# In[2]:


# Import Dataset
fname = 'data/stem.csv'
stem = pd.read_csv(fname, error_bad_lines=False)
# stem.head()
stem.count()
# stem.info()
# stem.reset_index(drop=True, inplace=True)


# In[3]:


stem_f_os_h = stem[(stem['Gender'] == 'female') & (stem['OverallScore'] >= 2.5)]
stem_f_os_h.reset_index(drop=True, inplace=True)
stem_f_os_l = stem[(stem['Gender'] == 'female') & (stem['OverallScore'] < 2.5)]
stem_f_os_l.reset_index(drop=True, inplace=True)

# In[4]:


stem_m_os_h = stem[(stem['Gender'] == 'male') & (stem['OverallScore'] >= 2.5)]
stem_m_os_h.reset_index(drop=True, inplace=True)
stem_m_os_l = stem[(stem['Gender'] == 'male') & (stem['OverallScore'] < 2.5)]
stem_m_os_l.reset_index(drop=True, inplace=True)

# In[5]:


stem_f_os_h.count()

# In[6]:


stem_f_os_l.count()

# In[7]:


stem_m_os_h.count()

# In[8]:


stem_m_os_l.count()

# In[9]:


stem_f_os_h.to_csv('data/Rating_Wise/OverallScore/stem_f_os_h.csv')

# In[10]:


stem_f_os_l.to_csv('data/Rating_Wise/OverallScore/stem_f_os_l.csv')

# In[11]:


stem_m_os_h.to_csv('data/Rating_Wise/OverallScore/stem_m_os_h.csv')

# In[12]:


stem_m_os_l.to_csv('data/Rating_Wise/OverallScore/stem_m_os_l.csv')
