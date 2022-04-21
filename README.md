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

The goal of this project was to identify factors affecting errors in the Zestimate used by Zillow to estimate single family home prices in 2017. The results of this project will be used to improve the model used to estimate prices and guide future data collection efforts. If we know log errors are higher for certain home characteristics we can investigate the reasons for higher errors, develop a mitigation plan, and improve model predictions. I used statistical testing, clustering and regression methods to provide insight into what affects log error. 

### Initial Questions and Hypotheses

1. Which categorical features have statistically significant absolute log errors greater than the overall mean?
    - Based on previous exploration some subsets of age, square footage, and location have higher than average log errors.  
2. Based on the results of 1, do any clusters of the following features result in meaningful insight into where log error is highest?
    - Clustering age, home size, and tax value
    - Clustering structure and land value
    - Clustering bathroom counts and bed to bathroom ratio
    - Clustering tax value, bathrooms, and tax delinquency statis
3. Can any of these clusters be used to help predict log error in a regression model?
    - Clusters can be used as inputs to the model


### Data Dictionary

| Variable    | Meaning     |
| ----------- | ----------- |
| bedroom    |  number of bedrooms in home         |
| bathroom           |  number of bathrooms in home          |
| bathroom_bin    |  number of bathrooms split into 3 categories     |
| bedroom_bin   |  number of bedrooms split into 3 categories     |
| age    |  age of the home   |
| square_feet    |  total living area of home    |
| tax_value           | total tax assessed value of the parcel (target) |
| fips    |  Federal Information Processing Standard code (location)       |
| bed_bath_ratio    |  ratio of bedrooms to bathrooms      |
| living_space   |  square footage - (bathrooms*40 + bedrooms*200)       |



### Project Plan

For this project I followed the data science pipeline:

Planning: I established the goals for this project and the relevant questions I wanted to answer. I used the results from my exploration to guide completion of this project. I followed similar steps as previous projects and used the Trello board from the Zillow regression project as a guide.

Acquire: The data for this project is from a SQL Database called 'zillow' located on a cloud server. The wrangle.py script is used to query the database for the required data tables and returns the data in a Pandas DataFrame. This script also saves the DataFrame to a .csv file for faster subsequent loads. The script will check if the zillow_2017.csv file exists in the current directory and if so will load it into memory, skipping the SQL query.

Prepare: The wrangle.py script uses the same wrangle_zillow function from the acquire step to prepare the data for exploration and modeling. Steps here include removing or filling in  null values (NaN), generating additional features, and encoding categorical variables. This script also contains a split_data function to split the dataset into train, validate, and test sets cleanly. Additional functions to remove outliers and scale the data are included in this file. The model.py file includes a function add_features to create additional features used in exploration and modeling.

Explore: The questions established in planning were analyzed using statistical tests including correlation and t-tests to confirm hypotheses about the data. This work was completed in the explore_zillow.ipynb file and relevant portions were moved to the improve_zillow.ipynb final deliverable. A visualization illustrating the results of the tests and answering each question is included. 

Model: Four different regression algorithms were investigated to determine if log errors could be predicted using features identified during exploration. A select set of hyperparameters were tested against train and validate data to determine which demonstrated the best performance. The final model was selected based on RMSE score on validate (after checking for overfitting) and used to make predictions on the withheld test data.

Delivery: This is in the form of this github repository as well as a presentation of my final notebook to the stakeholders.

### Steps to Reproduce

1. You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the zillow database. Store that env file locally in the repository. 
2. Clone my repository (including the wrangle_zillow.py and model.py modules). Confirm .gitignore is hiding your env.py file.
3. Libraries used are pandas, matplotlib, scipy, sklearn, seaborn, and numpy.
4. You should be able to run improve_zillow.ipynb.

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