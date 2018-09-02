class HeldWeapons():
	heldWeaponsList = []

class Weapons():

	weaponList = {
		'stick':{
			'title': "Stick",
			'sound': "*** whack whack whack ***",
			'damage': 1
		},
		'plunger':{
			'title': "Plunger",
			'sound': "*** Squish Plosh Squoosh ***",
			'damage': 2
		},
		'sword':{
			'title': "Sword",
			'sound': "*** SLASH!!! ***",
			'damage': 5
		}

	}

	def __init__(self, weapon):
		self.name = self.weaponList[weapon]
		self.title = self.name['title']
		self.sound = self.name['sound']
		self.damage = self.name['damage']

	def attacks(other):
		other.health = other.health - 1

	def __repr__(self):
		return "[{}, {}]".format(self.title, self.damage)

	def __str__(self):
		return "[{}, {}]".format(self.title, self.damage)