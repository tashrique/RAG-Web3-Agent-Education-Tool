from pytrends.request import TrendReq
import pandas as pd
import time
import random

# Initialize Google Trends API with simpler parameters
pytrends = TrendReq(hl='en-US', tz=360)

# Define search keywords (limit to fewer keywords to reduce chance of error)
keywords = ["Ethereum"]

try:
    # Add a small delay before making the request
    time.sleep(random.uniform(1, 3))
    
    # Fetch trends data with a more specific timeframe format
    pytrends.build_payload(
        kw_list=keywords, 
        timeframe='today 1-m',  # More reliable format: today 1-m for last month
        geo='',                 # Worldwide data
        cat=0                   # All categories
    )
    
    # Get interest over time
    trend_data = pytrends.interest_over_time()
    
    # Display the results
    if not trend_data.empty:
        print(trend_data)
    else:
        print("No data returned from Google Trends")
        
except Exception as e:
    print(f"Error fetching Google Trends data: {e}")
    print("Try reducing the number of keywords or using a different timeframe")
    
