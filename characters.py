import weapons

class Character(object):
	
	def __init__(self, name, health, magic, fatigue, attack):
		self.name = name
		self.health = health
		self.magic = magic
		self.fatigue = fatigue
		self.attack = attack


class Vampire(Character):
	
	def __init__(self, flight, bat, *args):
		self.flight = flight
		self.bat = bat
		super(Vampire, self).__init__(*args)

	def fly(self):
		if self.flight == 1:
			print("The Vampire Takes Flight")

	def bats(self):
		if self.bat == 1:
			print("The Vampire Transformed into a Bat")

	def get_stats(self):
		print("General Stats:")
		print(" Health: {}".format(self.health))
		print(" Magic: {}".format(self.magic))
		print(" Fatigue: {}".format(self.fatigue))
		print(" Attack: {}".format(self.attack))
		print("")
		print("Class Traits:")
		print(" Flight: {}".format(self.flight))
		print(" Bat: {}".format(self.bat))

	def attacks(self, other):
		print("{} Attacks!".format(self.name))
		other.health -= int(+1)

	def __repr__(self):
		return "Enemy Name: {}, Health:{}".format(self.name, self.health)

	def __str__(self):
		return "Enemy Name: {}, Health:{}".format(self.name, self.health)


class Blob(Character):

	def __init__(self, elasticity, duplicity, *args):
		self.elasticity = elasticity
		self.duplicity = duplicity
		super(Blob, self).__init__(*args)

	def duplicate(self, amount):					# this will divide blob heatlh by total number of separations
		self.health = self.health / amount
		

class Mold(Character):

	def __init__(self, growthAmount, disease, *args):
		self.growthAmount = growthAmount
		self.disease = disease
		super(Mold, self).__init__(*args)

	def grow(self):
		self.attack + 10


class Warrior(Character):

	def __init__(self, weapon, *args):
		self.weapon = weapons.Weapons(weapon)
		super(Warrior, self).__init__(*args)

	def attacks(self, player, other):
		#Weapons.attacks(other)
		other.health = other.health - player.weapon.damage

	def __repr__(self):
		return "Health:{} Weapon:{}".format(self.health, self.weapon)

	def __str__(self):
		return "Health:{} Weapon:{}".format(self.health, self.weapon)