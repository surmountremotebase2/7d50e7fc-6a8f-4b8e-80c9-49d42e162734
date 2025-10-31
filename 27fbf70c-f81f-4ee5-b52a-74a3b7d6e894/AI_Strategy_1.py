from surmount.base_class import Strategy, TargetAllocation

class RevenueGrowthStrategy(Strategy):
    def __init__(self):
        # Define a broad set of tickers to evaluate. In practice, this would likely be filtered based on market, sector, etc.
        self.tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "FB", "TSLA", "BRK.A", "V", "JNJ", "WMT"]

    @property
    def interval(self):
        # The interval might not directly apply if we're working with annual data, but required by the framework.
        return "1year" 

    @property
    def assets(self):
        # Return the list of tickers the strategy will evaluate.
        return self.tickers

    @property
    def data(self):
        # In a real scenario, this would include a data source capable of providing YoY revenue growth figures.
        return []

    def fetch_yoy_growth_data(self, ticker):
        # Placeholder for a method to fetch YoY revenue growth. This could involve API calls or database queries.
        # Returns YoY growth percentage as float for simplicity.
        # Example: return 0.05 for 5% growth
        # This is a mock function and needs real implementation based on your data source.
        return 0.05 

    def rank_stocks_by_growth(self, tickers):
        # Fetch YoY growth data and rank stocks.
        growth_data = {ticker: self.fetch_yoy_growth_data(ticker) for ticker in tickers}
        
        # Sort the dictionary by growth value in descending order and return sorted tickers.
        ranked_tickers = sorted(growth_data, key=growth_data.get, reverse=True)
        return ranked_tickers

    def run(self, data):
        # Rank the stocks based on YoY growth
        ranked_tickers = self.rank_stocks_by_growth(self.tickers)
        
        # Select the top 3 stocks
        top_3_tickers = ranked_tickers[:3]  # Assumes the list is sorted in descending order of growth
        
        # Assuming equal distribution of capital among the selected stocks
        if len(top_3_tickers) > 0:
            allocation_amount = 1 / len(top_3_tickers)
        else:
            allocation_amount = 0
        
        # Create and return the TargetAllocation object with allocations for the top 3 stocks
        return TargetAllocation({ticker: allocation_amount for ticker in top_3_tickers})

# Note: The functionality to fetch YoY growth data would need to be implemented based on the data source(s) you have access to.