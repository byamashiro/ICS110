def microbe_growth(initial_count,rate):
	growth = initial_count * rate
	return growth

projected_population = microbe_growth(10,100)
print(projected_population)


'''
def double(num):
    It is customary to comment functions
    using documentation strings (or docstrings)
    This function doubles any number you give it
    
    num = num * 2
    return num

double(42)
'''