# 🍽️ Restaurant Recommender System

A machine learning-based restaurant recommender system that suggests top restaurant options based on user preferences like cuisine, price range, and location. This project leverages content-based filtering and NLP techniques to provide personalized recommendations.

## 🔍 Project Overview

This system helps users discover restaurants tailored to their taste by analyzing:

* **Cuisine type**
* **Average cost for two**
* **Location**

It uses TF-IDF vectorization and **cosine similarity** to find restaurants with the most similar profiles to the user's preferences.

## 🧠 Key Features

* Combines cuisine, cost, and city data into a single feature set.
* Uses **TF-IDF** to convert text features into numerical vectors.
* Applies **cosine similarity** to recommend the most relevant restaurants.
* Simple, user-friendly function to get top N recommendations.

## 📊 Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn (TfidfVectorizer, Cosine Similarity)
* Natural Language Processing (NLP)

## 🛠️ How It Works

1. Dataset is cleaned and missing values are filled.
2. Features (`Cuisines`, `Average Cost for two`, `City`) are combined into a unified text field.
3. TF-IDF is applied to vectorize the combined features.
4. Cosine similarity is used to compute how similar each restaurant is to the user's input.
5. Top N most similar restaurants are returned as recommendations.

## 📅 Sample Input

```python
user_cuisine = 'Italian'
user_price_range = 'Medium'
user_location = 'Downtown'
recommend_restaurants(user_cuisine, user_price_range, user_location)
```

## 📄 Sample Output

Returns a list of recommended restaurants with:

* Name
* Cuisines
* Average Cost for Two
* City

## 📁 Dataset

The dataset includes columns like:

* `Restaurant Name`
* `Cuisines`
* `Average Cost for two`
* `City`
  *(Ensure you update the dataset path when running this locally.)*

## ✅ Future Improvements

* Add collaborative filtering for better personalization.
* Build a front-end UI for interactive recommendations.
* Integrate geolocation-based filtering.
