class animal:
	size = ''
	fur_color = ''

	def __init__(self, size, fur_color):
		self.size = size
		self.fur_color = fur_color

	#def __del__(self):
	#	print('Remember me, I was: ', self.size, 'and', self.fur_color)


class bird(animal):
	feather_shape = ''

	def shape(self, feather_shape):
		self.feather_shape = feather_shape



'''
	def color(animal):
		animal.fur_color = 'blue'
		print('The animal color is: ', animal.fur_color)
'''

#bird = animal('large','blue')

#print(bird.size,bird.fur_color)

