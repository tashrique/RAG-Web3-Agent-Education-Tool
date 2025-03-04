from pytrends.request import TrendReq
from typing import Dict, List, Any
from datetime import datetime

class TrendsService:
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)

    def get_trends(self, keywords = ['ethereum']) -> Dict[str, Any]:
        
        try:
            # First build the payload - this is required before making any requests
            self.pytrends.build_payload(
                kw_list=keywords[:5],  # Google Trends only allows up to 5 keywords
                timeframe='today 3-m'  # Last 3 months of data
            )
            
            # Get interest over time
            interest_data = self.pytrends.interest_over_time()
            
            if interest_data.empty:
                return {
                    "status": "error",
                    "message": "No trend data found for the specified keywords",
                    "data": None
                }
            
            # Convert the data to a more JSON-friendly format
            trend_data = {
                "keywords": keywords[:5],
                "timestamp": datetime.now().isoformat(),
                "trend_data": interest_data.reset_index().to_dict('records')
            }
            
            return {
                "status": "success",
                "message": "Successfully retrieved trend data",
                "data": trend_data
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error fetching trend data: {str(e)}",
                "data": None
            }

trends_service = TrendsService()