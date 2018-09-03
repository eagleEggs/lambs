import random
import game


class World():
	def __init__(self, levels, empty, bosses, chests, monsters, hiddenItems):
		self.levels = levels
		self.empty = empty
		self.bosses = bosses
		self.chests = chests
		self.monsters = monsters
		self.hiddenItems = hiddenItems

		@property
		def levels(self):
			return self.__levels

	def __repr__(self):
		return "Levels: {}".format(self.levels)

	def __str__(self):
		return "Levels: {}".format(self.levels)


class Biomes():

	biomeList = {
		'forest':{
			'rain': 1
		},
		'desert':{
			'rain': 0
		},
		'arctic':{
			'rain': 0
		}

	}

	def __init__(self, biome):
		self.biome = self.biomeList[biome]


def GenerateWorld(generatedWorld):

	level = []									# set up level array

	generated = generatedWorld

	#bossPlaced = 0
	iterate = int(generated.levels)
	while iterate > 0:
		for lev in range(0, iterate):					# replace array with random entities
			pick = random.randint(1, 6)
			if pick == 1:
				level.append("E")
				iterate = iterate - 1
			#if pick == 2 and bossPlaced == 0:           # originally set for one boss per level
			if pick == 2:
				level.append("B")
				#bossPlaced = 1
				iterate = iterate - 1
			if pick == 3:
				level.append("C")
				iterate = iterate - 1
			if pick == 4:
				level.append("M")
				iterate = iterate - 1
			if pick == 5:
				level.append("H")
				iterate = iterate - 1

	print("world Generated: {}".format(level))
	print("")
	regen = input("Regenerate? (y/n)")
	if regen == "y":
		game.Setup()
