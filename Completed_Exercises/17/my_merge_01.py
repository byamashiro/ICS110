import pandas as pd
import sys

left = pd.read_csv('left_file.csv')
right = pd.read_csv('right_file.csv')


left_right = pd.merge(left, right, on='name', how='inner')

left_right['matchip'] = left_right['toip'] == left_right['fmip']

#print(left_right['matchip'])
#sys.exit(0)

print(left_right[left_right['matchip'] == True])