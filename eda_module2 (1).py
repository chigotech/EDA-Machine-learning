#!/usr/bin/env python
# coding: utf-8

# In[2]:


# eda_module.py

import pandas as pd



import pandas as pd

def perform_eda(data):
   

    # Ensure that data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)

    # Check the type and content of the DataFrame
    print("Type of DataFrame:", type(data))
    print("Head of DataFrame:")
    print(data.head())

    # Display basic information about the dataset
    print("\nBasic Information about the Dataset:")
    print(data.info())

    # Display descriptive statistics
    print("\nDescriptive Statistics:")
    print(data.describe())

    # Display skewness and kurtosis
    print("\nSkewness:")
    print(data.skew())

    print("\nKurtosis:")
    print(data.kurtosis())

  


# In[ ]:




