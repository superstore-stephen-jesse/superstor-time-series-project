# This module acquires superstore data from acquire module and prepares it for exploration

import pandas as pd 
import numpy as np
import os 
import env
import acquire 

def prepare_superstore_data():
    
    df = acquire.get_superstore_data()
    
    return df