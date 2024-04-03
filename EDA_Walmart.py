#!/usr/bin/env python
# coding: utf-8

# # Title: 
# Exploratory Data Analysis (EDA) of Retail Store Weekly Sales Data

# # Objective: 
# To gain insights and understanding of the retail store's weekly sales data through exploratory analysis.

# # Problem Statement:
# Analyze the provided dataset to identify patterns, trends, and factors influencing weekly sales in the retail store.

# # Tools: 
# Python (Pandas, Matplotlib, Seaborn)

# In[1]:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:
df=pd.read_csv(r"C:\Users\Ritik Sonwane\OneDrive\Desktop\Walmart Data Analysis and Forcasting.csv")

# In[3]:
df

# In[6]:
df.head()

# In[5]:
df.describe()

# In[8]:
df.info()

# In[9]:
df.isnull().sum()

# In[22]:
df.columns


# # 1. What is the average weekly sales for each store?
# In[27]:
average_weekly_sales = df.groupby('Store')['Weekly_Sales'].mean()
print(average_weekly_sales)

# In[11]:
top_10_stores = average_weekly_sales.nlargest(10)
plt.figure(figsize=(10, 6))
top_10_stores.plot(kind='bar', color='skyblue')
plt.title('Top 10 Tiendas por Promedio de Ventas Semanales')
plt.xlabel('Tienda')
plt.ylabel('Promedio de Ventas Semanales')
plt.show()


# # Visualizing distribution of Weekly Sales
# In[28]:
plt.figure(figsize=(10, 6))
sns.histplot(df['Weekly_Sales'], kde=True)
plt.title('Distribution of Weekly Sales')
plt.xlabel('Weekly Sales')
plt.ylabel('Frequency')
plt.show()


# # 2. What is the total weekly sales for all stores?
# In[12]:
total_weekly_sales = df['Weekly_Sales'].sum()
print(f"Las ventas semanales totales para todas las tiendas son: {total_weekly_sales}")


# # 3. What is the standard deviation of weekly sales for all stores?
# In[13]:
std_dev_weekly_sales = df['Weekly_Sales'].std()
print(f"La desviación estándar de las ventas semanales para todas las tiendas es: {std_dev_weekly_sales}")

# In[34]:
plt.figure(figsize=(8, 6))
sns.violinplot(x=df['Weekly_Sales'], color='skyblue')
# Set title and labels
plt.title('Violin Plot of Weekly Sales')
plt.xlabel('Weekly Sales')
plt.show()

# In[15]:
plt.figure(figsize=(8, 6))
plt.hist(df['Weekly_Sales'], bins=20, color='royalblue', edgecolor='black')
plt.xlabel('Weekly Sales')
plt.ylabel('Frequency')
plt.title('Distribution of Weekly Sales')
plt.show()

# # 4. How many holiday weeks are there in the dataset?
# In[16]:
num_holiday_weeks = df[df['Holiday_Flag'] == 1]['Holiday_Flag'].count()
print("Number of holiday weeks:", num_holiday_weeks)

# In[17]:
num_holiday_weeks = df[df['Holiday_Flag'] == 1]['Holiday_Flag'].count()

# Create the bar chart
plt.figure(figsize=(8, 6))
plt.bar(['Holiday Weeks', 'Non-Holiday Weeks'], [num_holiday_weeks, len(df) - num_holiday_weeks], color=['royalblue', 'lightgray'])
plt.xlabel('Week Type')
plt.ylabel('Number of Weeks')
plt.title('Number of Holiday Weeks vs. Non-Holiday Weeks')
plt.show()

# # 5. What is the correlation between weekly sales and temperature?
# In[18]:
corr_sales_temp = df['Weekly_Sales'].corr(df['Temperature'])
print("Correlation between weekly sales and temperature:", corr_sales_temp)


# In[19]:
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Temperature', y='Weekly_Sales', color='royalblue', alpha=0.7)
sns.regplot(data=df, x='Temperature', y='Weekly_Sales', color='red', scatter=False)
plt.xlabel('Temperature')
plt.ylabel('Weekly Sales')
plt.title('Weekly Sales vs. Temperature with Regression Line')
plt.grid(True)
plt.show()

# In[20]:
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='Temperature', y='Weekly_Sales', hue='Weekly_Sales', palette='viridis', alpha=0.7)
plt.xlabel('Temperature')
plt.ylabel('Weekly Sales')
plt.title('Scatter Plot of Weekly Sales vs. Temperature')
plt.grid(True)
plt.show()


# # 6. What is the correlation between weekly sales and fuel price?
# In[21]:
corr_sales_fuel = df['Weekly_Sales'].corr(df['Fuel_Price'])
print("Correlation between weekly sales and fuel price:", corr_sales_fuel)


# # Visualizing Weekly Sales by Store
# In[30]:
plt.figure(figsize=(12, 6))
sns.barplot(x='Store', y='Weekly_Sales', data=df)
plt.title('Weekly Sales by Store')
plt.xlabel('Store')
plt.ylabel('Weekly Sales')
plt.show()
