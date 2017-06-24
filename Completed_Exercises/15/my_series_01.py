import pandas as pd
from pandas import Series

restaurant_ratings = Series([1,2,3,4,5], name='ratings', index=['mcd','burgerking','pandaex','roys','3660']) # Series(range(0,6))


print(restaurant_ratings['mcd'])
print(restaurant_ratings[['burgerking','pandaex','roys']])
