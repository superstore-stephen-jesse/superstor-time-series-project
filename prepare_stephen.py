# This module acquires superstore data from acquire module and prepares it for exploration

import pandas as pd 
import numpy as np
import os 
import env
from acquire_stephen import get_superstore_data

# import acquire_jesse

def prepare_superstore_data():
    
    df = get_superstore_data()
    
    # ========= NEED MORE PREPARE/CLEANING ===========
   
    # Index the datetime columns
    
    
    # Reset datetime index
    
    # Fill nulls 
    
    return df