import pandas as pd


left = pd.read_csv('left_file.csv')
right = pd.read_csv('right_file.csv')

left_right = pd.merge(left, right, on='name', how='inner')
left_right['matchip'] = left_right['toip'] == left_right['fmip']

bins = list(range(0, 1000001, 100000))
labels = ['one hundred thousand', 'two hundred thousand', 'three hundred thousand', 'four hundred thousand', 'five hundred thousand', 'six hundred thousand', 'seven hundred thousand', 'eight hundred thousand', 'nine hundred thousand', 'one million']

categories = pd.cut(left_right['payload'], bins, labels=labels)

left_right['bins'] = categories

print(left_right)

#tweet_view = league.pivot('timestamp', 'jleague', 'tweets')

pivot_lr = left_right.pivot('lat', 'long', 'bins')

print(pivot_lr)