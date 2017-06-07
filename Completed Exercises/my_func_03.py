def microbe_growth(initial_count, rate=1.05):
	growth = initial_count * rate
	return growth

projected_population = microbe_growth(10000)
print(projected_population)

high_projected_population = microbe_growth(10000,1.35)
print(high_projected_population)