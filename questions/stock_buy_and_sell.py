# I have an array stock_prices_yesterday where:

# The indices are the time, as a number of minutes past trade opening time, which was 9:30am local time.
# The values are the price of Apple stock at that time, in dollars.
# For example, the stock cost $500 at 10:30am, so stock_prices_yesterday[60] = 500.

# Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of 
# 1 Apple stock yesterday. For this problem, we won't allow shorting you must buy before you sell.


#stock_prices_yesterday = 

def get_best_profit(stock_prices_yesterday):
    min_price = stock_prices_yesterday[0]
    max_profit = 0
    for current_price in stock_prices_yesterday:
        min_price = min(min_price, current_price)
        max_profit = max(max_profit, current_price - min_price)
	
    print('Buy at {0} and sell at {1}'.format(min_price, max_profit))

get_best_profit([13,3,55,33,1,33,23])