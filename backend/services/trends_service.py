from pytrends.request import TrendReq
from typing import Dict, List, Any
from datetime import datetime

class TrendsService:
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)

    def get_trends(self, keyword):
        # keyword needs to be a list for pytrends
        if isinstance(keyword, str):
            keyword = [keyword]
            
        self.pytrends.build_payload(kw_list=keyword, timeframe='today 3-m')
        interest_data = self.pytrends.interest_over_time()
        
        if interest_data.empty:
            return {
                "status": "error",
                "message": "No trend data found for the specified keywords",
                "data": None
            }
        
        # Convert the data to a more JSON-friendly format
        trend_data = {
            "keywords": keyword,
            "timestamp": datetime.now().isoformat(),
            "trend_data": interest_data.reset_index().to_dict('records')
        }
        
        return {
            "status": "success",
            "message": "Successfully retrieved trend data",
            "data": trend_data
        }


trends_service = TrendsService()