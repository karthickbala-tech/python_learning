#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
# normal approach
x=[1,2,3,4,5,8,9]
y=[3.4,3,5,7,6,8,0]
plt.title('sample data')
plt.xlabel('data')
plt.ylabel('values')
plt.plot(x,y)
plt.show()


# In[ ]:


#object oriented approach
fig, ax=plt.subplots()
ax.plot(x,y)
ax.set_title("sample")
plt.show()


# types of plots

# In[ ]:


cars = {
    'bmw': 1050000,
    'audi': 2137622,
    'benz': 4654464,
    'toyota': 850000,
    'honda': 720000,
    'ford': 950000,
    'nissan': 680000,
    'chevrolet': 1020000,
    'volkswagen': 1150000,
    'kia': 630000,
    'hyundai': 700000,
    'mazda': 780000,
    'subaru': 820000,
    'jaguar': 3200000,
    'land_rover': 4500000,
    'tesla': 3800000,
    'porsche': 5500000,
    'ferrari': 12000000,
    'lamborghini': 15000000,
    'mercedes_gla': 3200000,
    'volvo': 900000,
    'mitsubishi': 650000,
    'suzuki': 580000,
    'lexus': 2600000,
    'acura': 2400000,
    'infiniti': 2100000,
    'mini': 800000,
    'peugeot': 720000,
    'renault': 690000,
    'citroen': 640000
}


# In[ ]:


fig , ax=plt.subplots()
ax,plot(cars.keys(),cars.values())
plt,show()


# In[ ]:


fig, ax = plt.subplots(figsize=(12,6))


# In[ ]:


#line plot
ax.plot(cars.keys(), cars.values(), marker='o' ,color='r')


# In[ ]:


#scatter plot
ax.scatter(cars.keys(), cars.values(), marker='o' ,color='r')


# In[ ]:


ax.hist(cars.keys(), cars.values(), marker='o' ,color='r')


# In[ ]:


#bar plot 
ax.bar(cars.keys(), cars.values(), color='skyblue')


# In[ ]:


#Horizontal Bar Plot
ax.barh(list(cars.keys()), list(cars.values()), color='orange')


# In[ ]:


#Step Plot
ax.step(cars.keys(), cars.values(), where='mid', color='green')


# In[ ]:


#Horizontal Bar PlotHorizontal Bar PlotHorizontal Bar Plot
ax.fill_between(cars.keys(), cars.values(), color='purple', alpha=0.3)
ax.plot(cars.keys(), cars.values(), color='green')


# In[ ]:





# In[ ]:


ax.set_title("Car Prices")
ax.set_xlabel("Car Brand")
ax.set_ylabel("Price (in currency units)")
plt.xticks(rotation=45, ha='right')  # rotate x labels for readability
plt.tight_layout()  # adjust layout so labels fit


# In[ ]:


plt.show()


# In[ ]:


prices = list(cars.values())


# In[ ]:


# Create a histogram
plt.figure(figsize=(10,6))
plt.hist(prices, bins=10, color='skyblue', edgecolor='black')  # bins = how many groups
plt.title("Distribution of Car Prices")
plt.xlabel("Price Range")
plt.ylabel("Number of Cars")
plt.show()


# subplots

# In[ ]:


fig, ax = plt.subplots(3, figsize=(12, 15)) 


# In[ ]:


ax[0].plot(cars.keys(), cars.values(), marker='o', color='r')
ax[0].set_title("Line Plot")
ax[0].set_ylabel("Price")
ax[0].tick_params(axis='x', rotation=45)


# In[ ]:


ax[1].bar(cars.keys(), cars.values(), color='g')
ax[1].set_title("Bar Plot")
ax[1].set_ylabel("Price")
ax[1].tick_params(axis='x', rotation=45)


# In[ ]:


ax[2].scatter(cars.keys(), cars.values(), color='b', marker='o')
ax[2].set_title("Scatter Plot")
ax[2].set_xlabel("Car Brand")
ax[2].set_ylabel("Price")
ax[2].tick_params(axis='x', rotation=45)


# In[ ]:


plt.tight_layout()  
plt.show()


# In[ ]:


import pandas as pd


# In[ ]:


csv_file = pd.read_csv("/home/parrot/Documents/machine_learning/datasets/dunya.csv")


# In[ ]:


x = csv_file['Country']
y1 = csv_file['Revenue']
y2 = csv_file['Nüfus']
y3 = csv_file['Per person']


# In[ ]:


plt.style.use('seaborn-v0_8')


# In[ ]:


fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(20, 12))


# In[ ]:


ax1.bar(x, y1, color='tab:blue', label='Revenue')
ax1.set_ylabel('Revenue')
ax1.legend()


# In[ ]:


ax2.bar(x, y2, color='tab:orange', label='Population')
ax2.set_ylabel('Population')
ax2.legend()


# In[ ]:


ax3.bar(x, y3, color='tab:green', label='Per Person')
ax3.set_ylabel('Per Person')
ax3.set_xlabel('Country')
ax3.legend()


# In[ ]:


plt.xticks(rotation=45, ha='right')
plt.suptitle("Income Comparison by Country", fontsize=18)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# enhance version

# In[ ]:


fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(20, 12))


# In[ ]:


ax1.bar(x, y1, color='tab:blue', label='Revenue')
ax2.bar(x, y2, color='tab:orange', label='Population')
ax3.bar(x, y3, color='tab:green', label='Per Person')


# In[ ]:


fig.legend(
    loc='upper right',
    bbox_to_anchor=(0.95, 0.95),
    title="Metrics"
)


# In[ ]:


ax1.set_ylabel('Revenue')
ax2.set_ylabel('Population')
ax3.set_ylabel('Per Person')
ax3.set_xlabel('Country')


# In[ ]:


plt.xticks(rotation=45, ha='right')
plt.suptitle("Income Comparison by Country", fontsize=18)
plt.tight_layout(rect=[0, 0, 0.9, 0.96])
plt.show()

