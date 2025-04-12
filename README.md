# BIG-DATA-ANALYSIS

COMPANY : CODETECH IT SOLUTIONS

NAME : GAUTAM VAID

INTERN ID : CT04DA594

DOMAIN : DATA ANALYTICS

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH

Fashion Brand Sales Data Analysis Using Dask
Project Overview
This project focuses on analyzing the sales data of a fashion brand using Dask, a parallel computing library, to efficiently handle large datasets. The goal was to clean, preprocess, and extract insights from the data to help the business make informed decisions related to product performance, customer behavior, and seasonal trends.

The dataset contains information about customer purchases, including:

CustomerID
Item 
Amount
Date  
Review 
Payment 

Technologies Used

-Python: Primary programming language.
-Dask: For distributed data processing to handle large datasets that may not fit into memory.
-Pandas: For data manipulation in conjunction with Dask.
-Matplotlib & Seaborn: (Optional) for visualization (if you decide to add visualization).
CSV Files: The format of the raw dataset.

Dataset Description
The dataset contains sales data for a fashion brand, with the following columns:
-CustomerID: Unique identifier for each customer.
-Item: The item purchased by the customer.
-Amount: The total price of the item(s) purchased.
-Date: Date when the purchase occurred.
-Review: Rating given by the customer for the purchased item.
-Payment: Method of payment used by the customer (e.g., Credit Card, Cash).

Objective
The primary objectives of this project were:
-Data Cleaning:
-Handle missing values.
-Convert data to the correct formats (e.g., datetime for Date).
-Save the cleaned data to a new CSV file.
-Exploratory Data Analysis (EDA):
-Perform EDA on the dataset to extract meaningful insights, including customer behaviors, product performance, monthly trends, and review ratings.

Customer Insights:
-Identify loyal and repeat customers.
-Analyze spending behaviors.
-Detect sensitive customers at risk of churn (e.g., high spend, low reviews).

Steps Involved
1. Data Loading
Objective: Load the raw CSV file and inspect its structure.
Method: Used dask.dataframe.read_csv() to load the dataset in a distributed manner.
Output: Previewed the first few rows using df.head().

2. Data Cleaning
Objective: Clean the data by addressing missing values and converting data to appropriate formats.
Filled Missing Values:
-Amount and Review columns were filled with the column's mean values.
Date Conversion:
-The Date column was converted to a datetime type to enable time-based analysis.
Save Cleaned Data:

The cleaned dataset was saved as Cleaned.csv for future analysis.

3. Exploratory Data Analysis (EDA)
Objective: Analyze the dataset to extract useful business insights.
-Calculate Total Sales:
The total sales (Amount) were computed to understand overall revenue.
-Average Review Rating:
The average review score across all items was calculated.
-Top 5 Items by Quantity:
Identified the top 5 most purchased items by quantity.
-Top 5 Items by Revenue:
Identified the top 5 items based on revenue generated.
-Monthly Sales Performance:
Aggregated sales by month to detect seasonal trends.
-Top Spenders:
Identified customers with the highest total spend.
-Consistent Spenders:
Identified customers with the most consistent spending (lowest variance in spending).
-Repeat Customers:
Detected repeat customers by counting their number of orders.
-Sensitive Customers:
Identified customers with high spend but low review ratings, which may indicate dissatisfaction or churn risk.
