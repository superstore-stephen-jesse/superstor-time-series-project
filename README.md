### This repository contains the code for the superstore time series project completed as part of the Codeup Data Science curriculum.

## Repo contents:
### 1. This Readme:
- Project description with goals
- Inital hypothesis/questions on data, ideas
- Data dictionary
- Project planning
- Instructions for reproducing this project and findings
- Key findings and recommendations for this project
- Conclusion
### 2. Final report (final_report.ipynb)
### 3. Acquire and prepare modules (acquire.py, prepare.py)
### 4. Exploration & modeling notebooks (explore_jesse.ipynb,explore_stephen.ipynb)
### 5. Functions to support exploration and modeling work (model.py)

### Project Description and Goals

The goal of this project was to provide recommendations for the VP of Product at a large office supplies store regarding product strategy going forward. We specifically looked at different product categories and customer segments to identify where we make our greatest profit and understand how this compares to sales volume.

### Initial Questions

1. Which product line should we expand?
2. Is there a product category that is particularly profitable?
3. Does one or anther stand out in terms of sales volume?
4. How do these relationships change if we control for customer segment?


### Data Dictionary

| Variable    | Meaning     |
| ----------- | ----------- |
| category    |  Product Category: Furniture, Office Supplies, or Technology       |
| sub_category           |  17 different products within each of the 3 categories         |
| segment    |  Customer Segment: Consumer, Corporate, or Home Office  |
| alpha   | Significance level, set to 0.05. Used for confidence level of statistical tests  |


### Project Plan

For this project we followed the data science pipeline:

Planning: We established the goals for this project and the relevant questions we wanted to answer. Similar steps from previous projects were used to scope out the project. As this was a group project we also established who was doing what to avoid duplicate work. 

Acquire: The data for this project is from a SQL Database called 'superstore_db' located on a cloud server. The acquire.py script is used to query the database for the required data tables and returns the data in a Pandas DataFrame. This script also saves the DataFrame to a .csv file for faster subsequent loads. The script will check if the superstore.csv file exists in the current directory and if so will load it into memory, skipping the SQL query.

Prepare: The prepare.py script has the prepare_superstore_data function to prepare the data for exploration and modeling. Steps here include removing or filling in  null values (NaN), removing unnessary columns, renaming columns, and changing data types as necessary. 

Explore: The questions established in planning were analyzed using statistical tests including t-tests to confirm hypotheses about the data. This work was completed in separate explore_stephen.ipynb and explore_jesse.ipynb files and relevant portions were moved to the final_report.ipynb final deliverable. A visualization illustrating the results of the tests and answering each question is included. 

Model: No explicit modeling was completed for this project.

Delivery: This is in the form of this github repository as well as a presentation of my final notebook to the stakeholders.

### Steps to Reproduce

1. You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the superstore_db database. Store that env file locally in the repository. 
2. Clone the repository. Confirm .gitignore is hiding your env.py file.
3. Libraries used are pandas, matplotlib, scipy, sklearn, seaborn, and numpy.
4. You should be able to run final_report.ipynb.

### Key Findings 

- Size, age, tax value and tax delinquency have the greatest effect on absolute log error.
- Older, smaller, and cheaper (tax value) homes have greater than average absolute error. Medium size and age homes have slightly lower average error. 

### Conclusion and Recommendations
- Based on the key findings demonstrated in this project efforts to improve the Zestimate should focus on the following home characteristics:
    - small size

### Future work

- Explore other factors that may affect log errors
- Create additional features and clusters for modeling
- Test additional hyperparameters for the models