#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pypllot as plt


# In[2]:


df = pd.read_csv("Real Estate.CSV")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[9]:


df[df.duplicated(subset = 'Property_ID')]


# In[13]:


df.drop_duplicates(inplace = True)


# In[18]:


df['Price'] = df['Price'].fillna(
    df['Price'].median()
)


# In[22]:


df['Area_sqft'] = df['Area_sqft'].fillna(
    df['Area_sqft'].median()
)


# In[23]:


df['Owner_Name'] = df['Owner_Name'].fillna(
    'Unknown Owner'
)


# In[24]:


df['Contact'] = df['Contact'].fillna(
    'Not Available'
)


# In[27]:


df["Price_Per_Sqft"] = (
df["Price"] / df["Area_sqft"]
)


# In[29]:


def Category(Price):
    if Price < 7000000:
        return "Budget"
    elif Price < 10000000:
        return "Mid Range"
    elif Price < 13000000:
        return "Premium"
    else:
        return "Luxury"

        df["Property_Category"] = (
            df["Price"].apply(Category)
        )


# In[32]:


df.to_csv (
"Real_Estate_Cleaned.CSV",
index = False
)


# In[ ]:


EDA.ipynb


# In[37]:


df['Price'].mean()
df['Area_sqft'].mean()
df['Bedrooms'].mean()

df.groupby('city')['Price].mean()
# In[39]:


df['City'].value_counts()


# In[40]:


df.nlargest (10, 'Price')


# In[43]:


sns.histplot(df['Price'])


# In[44]:


sns.barplot (
    x = 'City',
    y = 'Price',
    data = df
)


# In[46]:


sns.scatterplot (
    x = 'Area_sqft',
    y = 'Price',
    data = df
)


# In[50]:


sns.heatmap (
    df.corr(numeric_only = True),
    annot = True
    )


# In[53]:


df.to_csv("Real_Estate_Cleaned.csv", index = False)


# In[ ]:




