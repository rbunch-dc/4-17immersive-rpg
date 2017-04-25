class Hero(object):
	def __init__(self, name = "Incognito"):
		self.name = name
		self.health = 10
		self.power = 5

	def cheer_hero(self):
		print "Fight hard, %s" % self.name

	# this class method returns a boolean. True, if the hero is alive, false if the hero is dead
	def is_alive(self):
		return self.health > 0
		# if(self.health > 0):
		# 	return True
		# else:
		# 	return False