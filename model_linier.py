#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
#import statsmodels.api as sm
#import statsmodels.formula.api as smf

# Assign url of file: url
alamat = 'mtcars.csv'

# Read file into a DataFrame: df
df = pd.read_csv(alamat)

# Print the head of the DataFrame
print(df.head())


# In[9]:


x=df['drat']
y=df['qsec']
kemiringan,konstanta,r_value,p_value,std_err = stats.linregress(x,y)
garis_regresi=kemiringan*x+konstanta

fig, (ax1) = plt.subplots(1)
ax1.scatter(x,y,color='#4D0132')
ax1.plot(x,garis_regresi,color='red')
plt.xlabel('disp')
plt.ylabel('mpg')

#cek apakah mean dari residual = 0?
#cek apakah variansi error konstan?
fig, (ax1) = plt.subplots(1)
ax1.scatter(x,y-garis_regresi,color='#4D0132')
plt.ylabel('residual')


# In[10]:


x=df['drat']
y=df['qsec']
kemiringan,konstanta,r_value,p_value,std_err = stats.linregress(x,y)
garis_regresi=kemiringan*x+konstanta

fig, (ax1) = plt.subplots(1)
ax1.scatter(x,y,color='#4D0132')
ax1.plot(x,garis_regresi,color='red')
plt.xlabel('disp')
plt.ylabel('drat')

fig, (ax1) = plt.subplots(1)
ax1.scatter(x,y-garis_regresi,color='#4D0132')
ax1.plot(x,np.zeros(len(x)),color='red')
plt.ylabel('residual')


# In[11]:


from scipy.stats import pearsonr
korelasi_pearson, pvalue=pearsonr(df['drat'], df['qsec'])
print(korelasi_pearson)


# In[12]:


from scipy.stats import spearmanr
korelasi_spearman, pvalue=spearmanr(df['drat'], df['qsec'])
print('Korelasi spearman = %.2f' %korelasi_spearman)


# In[13]:


korelasi_wtdrat, pvalue=pearsonr(df['wt'], df['drat'])
korelasi_mpgdisp, pvalue=pearsonr(df['mpg'], df['disp'])

fig, (ax1) = plt.subplots(1)
ax1.scatter(df['wt'],df['drat'],color='#4D0132')
plt.xlabel('wt')
plt.ylabel('drat')
plt.title('korelasi = %.2f' %korelasi_wtdrat)

fig, (ax1) = plt.subplots(1)
ax1.scatter(df['mpg'],df['disp'],color='#4D0132')
plt.xlabel('mpg')
plt.ylabel('disp')
plt.title('korelasi = %.2f' %korelasi_mpgdisp)


# In[14]:

x = 'qsec'
y = 'disp'

#BAGIAN INI PAHAM MAKSUD DARI KODE TERSEBUT
pearson_wtdrat, pvalue=pearsonr(df[x], df[y])
spearman_wtdrat, pvalue=spearmanr(df[x], df[y])

fig, (ax1) = plt.subplots(1)
ax1.scatter(df[x],df[y],color='#4D0132')
plt.xlabel(x)
plt.ylabel(y)
plt.title('pearson = %.2f, spearman = %.2f' %(pearson_wtdrat, spearman_wtdrat))




# In[15]:


import statsmodels.api as sm

results = sm.OLS(y, x).fit()
print(results.summary())



