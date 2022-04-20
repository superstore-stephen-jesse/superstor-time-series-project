# This module acquires superstore data from acquire module and prepares it for exploration

import pandas as pd 
import numpy as np
import os 
import env
from acquire_stephen import get_superstore_data
import datetime 

# import acquire_jesse

def prepare_superstore_data():
    # Call the acquire data data function
    df = get_superstore_data()
    
    # Lower camel-cased df columns names lower
    df = df.rename(columns = str.lower)
    
    # Strip spaces in columns names 
    df.columns = df.columns.str.replace(' ','_')
        
    # Drop Unnecessessary columns 
    df = df.drop(columns = ['region_id','product_id','customer_id','category_id','order_id'])
    
    # Engineer columns names 
    df = df.rename(columns={'sub-category':'sub_category'})
    
    # Index the datetime columns
    df.order_date = pd.to_datetime(df.order_date)
    df.ship_date = pd.to_datetime(df.ship_date)

    
    
    # Reset datetime index
    
    # Fill nulls 
    
    return df