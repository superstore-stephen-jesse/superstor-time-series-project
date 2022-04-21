import pandas as pd 
import env
import os 

def db_conn_url():
    '''
        SQL Database connection function (Calls the env.py file to acquire login info) 
    '''
    db = 'superstore_db'
    
    url = f'mysql+pymysql://{env.username}:{env.password}@{env.host}/{db}'
        
    return url

def get_superstore_data(use_cache = True):
    '''
        Function uses cache to ensure no local file is saved in local machine. If not, 
        calls the sql connection to CodeUp databses and downloads csv file. Saves local 
        file for future calls.
    '''
    superstore = 'superstore.csv'
    
    if os.path.exists(superstore) and use_cache:
        
        print('Reading csv file..')
        
        return pd.read_csv(superstore)
    
    qry = '''
    
            SELECT *
            FROM orders
            JOIN categories
            USING (`Category ID`)
            JOIN customers
            USING (`Customer ID`)
            JOIN products
            USING (`Product ID`)
            JOIN regions
            USING (`Region ID`);
    
          '''
    print('Getting data from SQL database..')
    
    df = pd.read_sql(qry, db_conn_url())
    
    print('Caching csv file locally..')
    
    df.to_csv(superstore, index = False)
    
    # Returns df
    return df
    
    
        
    