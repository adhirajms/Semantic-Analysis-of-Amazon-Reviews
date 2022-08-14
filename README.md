# Semantic-Analysis-of-Amazon-Reviews

This project is a part of the Big Data Platforms Course (MScA 31013) at the University of Chicago's Master's of Science in Analytics Program.  


## Project Intro/Objective
The purpose of this project is to analyze Amazon products’ review data to provide business insights and actionable suggestions for product improvement. 

### Methods Used
* Neural Networks
* Machine Learning
* Data Visualization
* Predictive Modeling


### Technologies
* Python
* Google Cloud Platforms
* PySpark
* Excel

## Dataset
The data has been acquired from https://nijianmo.github.io/amazon/index.html.

We selected the data of the categories- 'Fashion & Clothing', 'Jewellery & Shoes', 'Luxury Beauty', and 'All Beauty'. For each product within the category, we contain multiple features including the review text, the rating, the date of the review, the price.

## Methodology

As a part of cleaning the data, we applied a 10 core filtering on the dataset which removed all products which had lesser than 10 reviews and dropped all rows where reviewText was missing. As on of the main aims of this project was to understand the trend in review sentiment over time and model the relationship between text and ratings, we applied multiple text analysis pipeline to derive insights from the review text data.

### Pipeline 1 : 
Converting review text into TF-IDF vector representation for regression modelling with ratings. The steps followed here include tokenisation, lammetization, removing stop words and creating n-grams.

#### Pipeline 2 : 
Extracting keywords and sentiment from review Text. All the steps to clean the data are followed from the first pipeline.

After EDA and feature engineering, we used  different models to predict the reviews' star rating:
- Binary Logistic Regression
- Multi-class Logistic Regression
- Random Forest
- Linear SVM
- Gradient Boosting Classifier

Additionally, we also created a timeline of sentiment for each product providing insights into how product feature changes are being perceived by the customers. The keywords were then plotted on a word cloud to provide a snapshot of reviews.

## Contributing Members

|Name     |  GitHub Handle   | 
|---------|-----------------|
|[Adhiraj M Srivastava](https://github.com/adhirajms) |     @adhirajms   |
|[Shikhar Madrecha](https://github.com/madrechashikhar)| @madrechashikhar        |
|[Vanshika Tibarewalla](https://github.com/vanshikatib95) |     @vanshikatib95    |
|[Jingjing Li ](https://github.com/syb8)| @syb8        |
