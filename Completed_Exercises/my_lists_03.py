alphalist = ['a','b','c'] + ['x','y','z']
alphalist.append(['o','p','q'])

print(alphalist)

del alphalist[6]

alphalist.extend(['G','g','G'])
print(alphalist)

alphalist.sort(key = str.upper)
print(alphalist)