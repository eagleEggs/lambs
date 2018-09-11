import weapons
import characters


def GenerateEnemyList():
	enemyList = (characters.Vampire, characters.Blob, characters.Mold)
	return enemyList

class Character(object):
	def __init__(self, name, health, magic, fatigue, attack, level):
		self.name = name
		self.health = health
		self.magic = magic
		self.fatigue = fatigue
		self.attack = attack
		self.level = level
		self.specials = []

	def card(self):

		print("########################")
		print("## Name:     {}       ".format(self.name))
		print("## Level:    {}       ".format(self.level))
		print("## Health:   {}       ".format(self.health))
		print("## Fatigue:  {}       ".format(self.fatigue))
		print("## Magic:    {}       ".format(self.magic))
		for special in self.specials:
			print("## Special:  {}   ".format(special))
		print("########################")


class Vampire(Character):
	
	def __init__(self, flight=False, bat=False, *args):
		super(Vampire, self).__init__(*args)
		self.flight = flight
		self.bat = bat
		if flight:
			self.specials.append("Flight")
		if bat:
			self.specials.append("Bat")

	def fly(self):
		print("The Vampire Takes Flight")

	def bats(self):
		print("The Vampire Transformed into a Bat")

	def attacks(self, other):
		print("{} Attacks!".format(self.name))
		other.health -= int(+1)

	def avatar(self):
		print("""\
             ^--^
	    |-_-|
	   (     )
	  |      |
	 |       |
	|       |
	""")
		self.card()

	def __repr__(self):
		return "Enemy Name: {}, Health:{}".format(self.name, self.health)

	def __str__(self):
		return "Enemy Name: {}, Health:{}".format(self.name, self.health)


class Blob(Character):

	def __init__(self, duplicate=False, steal=False, *args):
		super(Blob, self).__init__(*args)
		self.duplicate = duplicate
		if duplicate:
			self.specials.append("Duplicate")
		if steal:
			self.specials.append("Steal")

	def duplicate(self, amount):					# this will divide blob heatlh by total number of separations
		self.health = self.health / amount

	def avatar(self):
		print("""\

	  ./ -_-\.
	    ____/

""")
		self.card()
		

class Mold(Character):

	def __init__(self, growth=False, disease=False, *args):
		super(Mold, self).__init__(*args)
		self.growth = growth
		self.disease = disease
		if growth:
			self.specials.append("Growth")
		if disease:
			self.specials.append("Disease")

	def grow(self):
		self.attack + 10

	def avatar(self):
		print("""\
	   |^^^^|
	   / 0.o|
	  <      >
	   \<__>/

	   """)
		self.card()


class Warrior(Character):

	def __init__(self, weapon, *args):
		self.weapon = weapons.Weapons(weapon)
		super(Warrior, self).__init__(*args)

	def attacks(self, player, other):
		other.health = other.health - player.weapon.damage

	def __repr__(self):
		return "Health:{} Weapon:{}".format(self.health, self.weapon)

	def __str__(self):
		return "Health:{} Weapon:{}".format(self.health, self.weapon)

