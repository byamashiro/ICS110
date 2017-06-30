import pandas as pd
import time
start_time = time.clock()

# Read the data from each file into separate pandas DataFrames using the .read_csv() method
daily = pd.read_csv('AMEX_daily_prices_N.csv')
dividends = pd.read_csv('AMEX_dividends_N.csv')

# Display to the screen the first 7 rows of each DataFrame
print(daily.head(7))
print(dividends.head(7))


#print('=' * 30)

# merge on the stock_symbol column, as the key
# merge using an inner join
df1 = pd.merge(daily, dividends, on='stock_symbol', how='inner')


# Identify any stocks with a Dividend Date (NOT a Daily Price Date) of 1991-06-24
# Display to the screen the unique symbol(s) for stocks with that date.
#print(df1)
#print(df1[df1['date_y'] == '1991-06-24'])
print(df1[df1['date_y'] == '1991-06-24'].stock_symbol.unique())


end_time = time.clock()

print('Time elapsed: ', (end_time - start_time))