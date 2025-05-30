# -*- coding: utf-8 -*-
"""Restarant -Recommender.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/110bhN7Vt6dWzC82Jbett9UfgsatTaCrJ
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv('/content/Dataset  (1).csv')

# Display the first few rows
df.head()

# Check for missing values
print(df.isnull().sum())

# Fill or drop missing values based on your strategy
df.fillna('', inplace=True)

# View column names to decide which to use
print(df.columns)

print(df.columns.tolist())

print(df.columns.tolist())

['Restaurant Name', 'Cuisines', 'Average Cost for two', 'City']

df['combined_features'] = df['Cuisines'].astype(str) + ' ' + df['Average Cost for two'].astype(str) + ' ' + df['City'].astype(str)

def recommend_restaurants(user_cuisine, user_price_range, user_location, top_n=5):
    user_input = user_cuisine + ' ' + user_price_range + ' ' + user_location
    user_vec = vectorizer.transform([user_input])

    sim_scores = cosine_similarity(user_vec, feature_matrix).flatten()
    top_indices = sim_scores.argsort()[-top_n:][::-1]

    return df.iloc[top_indices][['Restaurant Name', 'Cuisines', 'Average Cost for two', 'City']]

vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(df['combined_features'])

# Compute cosine similarity between restaurants
similarity = cosine_similarity(feature_matrix)

def categorize_price(price):
    if price <= 300:
        return 'Low'
    elif price <= 600:
        return 'Medium'
    else:
        return 'High'

df['price_category'] = df['Average Cost for two'].apply(categorize_price)

# Sample user preferences
user_cuisine = 'Italian'
user_price_range = 'Medium'
user_location = 'Downtown'

# Get recommendations
recommendations = recommend_restaurants(user_cuisine, user_price_range, user_location)
print("Top Recommended Restaurants:")
print(recommendations)