#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# <b>1. Wczytać plik csv.</b>

# In[2]:


df = pd.read_csv("dane.csv")


# In[3]:


df.head()


# <b> 2. Znaleźć client_id, closed_volume oraz reg_date dla transakcji, na której był największy profit. </b>

# In[4]:


max_profit_row = df[df['profit']== df['profit'].max()]
print(max_profit_row)


# In[5]:


max_profit_row[['client_id','closed_volume','reg_date']]


# <b>3. Stworzyć nową tabelę z pogrupowanymi danymi. Kolejne kolumny to:</b>
# - client_id
# - suma profitu danego klienta
# - średni wolumen na transakcji
# - liczba transakcji klienta
# - data rejestracji klienta
# 
# <b>przykładowy wiersz: [client_id, sum(profit), avg(closed_volume), reg_date] = [123156, 1235, 111, 1500000000000]
# </b>

# In[6]:


df2 = df.groupby('client_id').agg({'profit': 'sum', 'closed_volume': ['mean','count'], 'reg_date':'min' })


# In[7]:


df2.columns = ['sum(profit)', 'avg(closed_volume)', 'count(transactions)', 'reg_date']


# In[8]:


df2.head()


# <b>4. Stworzyć zmienną reg_date_bin, która przyjmuje 1 gdy data rejestracji jest większa niż 1515000000000,
#  i 0 w przeciwnym przypadku.</b>

# In[9]:


df['reg_date_bin']=df['reg_date'].apply(lambda x: 1 if x > 1515000000000 else 0)


# <b> 5. Stworzyć model regresji liniowej, gdzie zmienną zależną będzie suma profitu, a niezależną średni wolumen,
# liczba transakcji oraz binarna zmienna reg_date_bin (w modelu uwzględnić stałą). Sprawdzić istotność zmiennych.</b>

# In[10]:


# y: sum(profit)
# x : avg(closed_volume) , count(transactions) , reg_date_bin, constant


# In[11]:


df2['reg_date_bin']=df2['reg_date'].apply(lambda x: 1 if x > 1515000000000 else 0)


# In[12]:


import statsmodels.api as sm


# In[13]:


X = df2[['avg(closed_volume)','count(transactions)', 'reg_date_bin']] 
Y = df2['sum(profit)']
X = sm.add_constant(X) # add a constant
model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 

print(model.summary())


# In[14]:


print("""H0: There is little to no statistical relationship between dependent and independent variable.
If P value less than the confidence level, assume 0.05, there is a statistically significant relationship between the term and the response.\n""")
print ("Variables significance test results: \n")
print ("As we can see from the above summary, assuming 0.05 confidence level,")
print ("We can reject H0 for avg(closed_volume) and count(transactions).")
print ("On the other hand, we fail to reject H0 for const and reg_date_bin .")


# <b>6. Sprawdzić dopasowanie modelu do danych za pomocą jednej (dowolnie wybranej) miary.</b>
# 

# In[15]:


ProbF= 4.02e-69 
print ("Model fit test: \n") 
print ("The Prob (F-statistic) in the model:", "{:.69f}".format(ProbF) ,"is much lower than significance level 0.005.") 
print("\nThis implies that the regression model fits the data way better than model with no independent variables")


# <b>7. Dopasować rozkład normalny do zmiennej profit w pierwotnym pliku dane (polecamy utworzyć obiekt 
#  norm z pakietu scipy.stats, dla rozjaśnienia sytuacji polecamy również wykonać histogram profitu z transakcji).
#  Na tej podstawie policzyć prawdopodobieństwo, że profit z transakcji będzie większy niż 1000. </b>

# In[16]:


profit_dist = list(df['profit'])


# In[17]:


from scipy.stats import norm

# Fit a normal distribution to the data:
mu, std = norm.fit(profit_dist)

# Plot the histogram.
plt.hist(profit_dist, bins=25, density=True, alpha=0.6, color='g')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)

plt.show()


# In[18]:


#Probability of profit more than 1000 from scipy:    
less_than_value = norm.cdf(1000, loc = -10.55, scale = 423.41)
# 1- Pr(less_than_value) for Pr(more_than_value)
more_than_value = 1-less_than_value
print ("Probability of profit being more than 1000 estimated at" , "{:.4f}".format((more_than_value)),"%" )


# <b>Bonus: </b>

# In[19]:


#Graphial representation of variables regression showing high correlation of transaction count and profits
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.plot_partregress_grid(model, fig=fig)


# In[20]:


# Plotted data below and R^2 at 0.994 confirms a good fit of the model
plt.plot(X, Y, 'o', label="data")
plt.plot(X, model.fittedvalues, 'x', label="OLS")

