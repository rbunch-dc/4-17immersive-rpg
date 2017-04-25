# Import the Hero class from Hero.py
from Hero import Hero
# Import the Goblin class from Goblin.py
from Goblin import Goblin
from Vampire import Vampire

# Ask the user for the hero's name
print ("What is thy name, brave adventurer?")
hero_name = raw_input("> ")
the_hero = Hero(hero_name)
# the_hero.cheer_hero()
monsters = []
monsters.append(Goblin())
monsters.append(Vampire())

# print "How many monsters are you willing to fight?"
# number_of_enemies = raw_input("> ")

# for i in range(0,len(monsters)-1)
# monsters[i]

for monster in monsters:
	print "Brave %s, you have encountered a %s." % (the_hero.name,monster.name)
	# Run game as long as BOTH cahracters have health
	while monster.health > 0 and the_hero.is_alive():
	 	print "You have %d health and %d power." % (the_hero.health, the_hero.power)
	 	print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
	 	print "What do you want to do?"
	 	print "1. Fight %s" % monster.name
	 	print "2. Do nothing"
	 	print "3. Flee"
	 	print "4. Drink potion of life"
	 	print "> ",
	 	user_input = raw_input()
	 	if (user_input == "1"):
	 		# Hero is goign to attack
	 		# the_goblin.health -= the_hero.power
	 		# the_hero.attack(the_goblin)
	 		monster.take_damage(the_hero.power)

	 		print "You have done %d damage to the %s" % (the_hero.power,monster.name)
	 		if monster.health <= 0:
	 			print "You have defeated the %s!" % monster.name
	 			the_hero.xp += monster.xp_value
	 			the_hero.check_level()
	 	elif user_input == "2":
	 		# Hero is going to do nothing
	 		pass
		elif user_input == "3":
			print "Goodbye, coward"
			break
		elif user_input == "4":
			the_hero.increase_health(20)
		else:
			print "Invalid input %s" % user_input

		if monster.health > 0:
			# hero has attacked (or not) AND goblin is still alive
			the_hero.health -= monster.power
			print "The goblin hits you for %d damage" % monster.power
			if the_hero.health <= 0:
				print "You have been killed by the goblin."
		if the_hero.health > 0 and the_hero.health < 5:
			print "You have gone into a rage. Your power has increased!"
			the_hero.power += 5
