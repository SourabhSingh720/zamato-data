# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 20:20:34 2022

@author: forev
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('HyderabadResturants.csv')
# =============================================================================
# print(df.head)
#print(df.columns)
def rate(r):
    if(r=='New' or r=='-'):
        return np.nan
    else:
        r=str(r).split('/')
        r=r[0]
        return float(r)
df['ratings']=df['ratings'].apply(rate)
df['ratings'].fillna(round(df['ratings'].mean()))

df['ratings'].replace(to_replace=[('New'),('-')],value='np.nan')

df['ratings']=df['ratings'].fillna(df['ratings'].mean())

#print(df['ratings'].unique())
# print(df.isnull().any())


# =============================================================================
df1=df.drop('links',axis=1)
#print(df.dtypes)

#print(df1.head)
#print(df1['price for one'].describe())

#df1.boxplot('price for one')

df2=df1.groupby('cuisine',as_index=False)['price for one'].count().nlargest(20,columns='price for one')
df3 = df2[:6].copy()



#others
new_row = pd.DataFrame(data = {
    'cuisine' : ['others'],
    'price for one' : [df2['price for one'][6:].sum()]
})

#combining top 5 with others
df4 = pd.concat([df3, new_row])

ax1=df4.plot(kind='pie',title='Maximum Ordered',labels=df4['cuisine'],y='price for one',legend=False,autopct='%1.1f%%')
ax1.set_ylabel('')


#print(df3)

plt.show()

#print(df1['cuisine'].describe())


df5=df1.groupby('cuisine')['ratings'].mean().nlargest(10)
print(df5)
df6=df5.plot(kind='bar',title='Ratings')
df6.set_ylim([4.3,4.5])

plt.show()



