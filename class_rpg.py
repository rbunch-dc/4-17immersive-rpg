# Import the Hero class from Hero.py
from Hero import Hero
# Import the Goblin class from Goblin.py
from Goblin import Goblin

the_hero = Hero("Aragon")
# the_hero.cheer_hero()
the_goblin = Goblin()


# Run game as long as BOTH cahracters have health
while the_goblin.health > 0 and the_hero.is_alive():
 	print "You have %d health and %d power." % (the_hero.health, the_hero.power)
 	print "The goblin has %d health and %d power." % (the_goblin.health, the_goblin.power)
 	print "What do you want to do?"
 	print "1. fight goblin"
 	print "2. do nothing"
 	print "3. flee"
 	print "> ",
 	user_input = raw_input()
 	if (user_input == "1"):
 		# Hero is goign to attack
 		the_goblin.health -= the_hero.power
 		print "You have done %d damage to the goblin" % the_hero.power
 		if the_goblin.health <= 0:
 			print "You have defeated the goblin!"
