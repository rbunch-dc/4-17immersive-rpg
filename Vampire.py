# Import the Monster class
from Monster import Monster
class Vampire(Monster):
	def __init__(self):
		super(Vampire, self).__init__("The name we want to use - first arg")
		self.health = 12
		self.power = 5
		# self.name = "Vampire"
		self.xp_value = 10
