import pandas as pd
import numpy as np
import os
from env import get_db_url

def acquire_data():
    filename = './superstore.csv'
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        return df
    else:
        query = """SELECT *
        FROM orders
        JOIN categories
        USING (`Category ID`)
        JOIN customers
        USING (`Customer ID`)
        JOIN products
        USING (`Product ID`)
        JOIN regions
        USING (`Region ID`);"""
    
        df = pd.read_sql(query, get_db_url('superstore_db'))
        
        df.to_csv(filename, index = None)
        
        return df