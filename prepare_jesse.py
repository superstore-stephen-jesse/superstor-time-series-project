import pandas as pd


def prepare_superstore(df):
    """ Prepare superstore data by renaming columns, converting data types, and dropping foreign keys"""
    
    # Converts column names to lower case and changes spaces to underscores
    df.columns = [col.lower().replace(" ","_") for col in df.columns]
    
    # Convert dates to pd.datetime format
    df.order_date = pd.to_datetime(df.order_date)
    df.ship_date = pd.to_datetime(df.ship_date)
    
    # Drop unnecessary foreign keys
    df = df.drop(columns = ['region_id','category_id'])
    
    return df