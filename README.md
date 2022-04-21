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
### 4. Exploration & modeling notebooks (explore_jesse.ipynb, explore_stephen.ipynb)

### Project Description and Goals

The goal of this project was to provide recommendations for the VP of Product at a large office supplies store regarding product strategy going forward. We specifically looked at different product categories(including sub-categories) and customer segments to identify areas where we can maximize company profit and understand how this compares to sales volume.

### Initial Questions

1. Which product line should we expand?
2. Is there a product category that is particularly profitable?
3. What product category is least profitable, why?
4. Does one or anther stand out in terms of sales volume?
5. How do these relationships change if we control for customer segment?


### Data Dictionary

| Variable    | Meaning     |
| ----------- | ----------- |
| category    |  Product Category: Furniture, Office Supplies, or Technology       |
| sub_category           |  17 different products within each of the 3 categories         |
| segment    |  Customer Segment: Consumer, Corporate, or Home Office  |
| alpha   | Significance level, set to 0.05. Used for confidence level of statistical tests  |


### Project Plan

For this project we followed the data science pipeline:

__Planning:__ We established the goals for this project and the relevant questions we wanted to answer though brain-stomming and several zoom calls. Most conceptual steps from  were used to scope out the project. As this was a group project we also established work assignements from the start go to avoid duplicate work. Adapted agile work-flow format.

__Acquire:__ The data for this project is from a SQL Database called 'superstore_db' located on a cloud server. The acquire.py script is used to query the database for the required data tables and returns the data in a Pandas DataFrame. This script also saves a local cached DataFrame to a 'superstore.csv' file for faster subsequent loads. The script will check if the superstore.csv file exists in the current directory and if so will load it into memory, skipping the SQL query. Initial DataFrame
contained 1734 rows and 22 columns.

__Prepare:__ The prepare.py module has the prepare_superstore_data function to prepare the data for exploration and modeling. Steps here include renaming the original columns to a consistent lowercase names, strip spaces from column names and instead separate names with '_' character, drop unnecessary columns  with suffix ..'id', index the order date columns to pandas datetime and reset index on the same order date column. Lastly, filled null, if any, with 0. 

__Explore:__ The questions established in planning were analyzed using statistical tests including t-tests to confirm hypotheses about the data. This work was completed in separate explore_stephen.ipynb and explore_jesse.ipynb files and relevant portions were moved to the final_report.ipynb final_report and slides deliverables as outlined in the project scope. A visualization illustrating the results of the tests and answering each question is included. 

__Model:__ No explicit modeling was completed for this project as per project guidelines. However, the recommendations suggested are backed by verifiable evidence inferred from data.

__Delivery:__ A recorded presentation will be submitted with a clear recommendation to the VP of Product as the main stakeholder. Other deliverables include: This github repository. Link found in the appendix section of this README.md file.

### Steps to Reproduce

1. You will need a locally stored env.py file that contains the hostname, username/user and password of the mySQL database that contains the 'superstore_db' database (copy hosted by CodeUp, San Antonio, TX).  
2. Clone the repository. 
3. Confirm '.gitignore' is maintaining secure login integrity by ocluding public share of server access credentials.  
4. Libraries used are pandas, matplotlib, scipy, sklearn, seaborn, and numpy.
5. With these, steps followed, you should be able to run final_report.ipynb.

### Key Findings 

- Technology product category is the most profitable. 
- Least profitable category is the furniture(making loses).
- Most profitable sub-categories are copiers, Accessories, and Chairs and least profitable (incurring loss) being Machines, Bookcases, and Tables.
- Home office and consumer segments with combination with Technology are very profitable.
- High sales volume does not equate to higher profits.


### Conclusion and Recommendations
- We should improve our technology offerings as this is our most profitable product category
- Concentrate on most profitable customer segments and product category, notably:
       - Technology: Home Office and Consumer (average profit is > 3 x overall average)
- Re-evaluate furniture sales as this is our least profitable product category (average loss in this category) despite having one of the highest sales volumes.


### Future work

- Evaluate products sold by region and how they vary
- Evaluate discount and ship date and how these factors affect profit 
- Create model that can predict future frofits accurately 

### Appendix

Project GitHub Repository: https://github.com/superstore-stephen-jesse/superstore-time-series-project.git
##### Credits:
- Jesse Marder, Data Scientist
    - https://github.com/jesse-d-marder
- Stephen Kipkurui, Data Scientist
    - https://github.com/stephenkipkurui
