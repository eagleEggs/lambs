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


class Map(World):


	def __init_(self, home, castle, emptyHorizontal, filledHorizontal):
		self.char = self.char
		self.home = self.mapHouse
		self.casle = self.mapCastle
		self.emptyHorizontal = self.mapEmptyHorizontal
		self.filledHorizontal = self.mapFilledHorizontal

	def mapHome():


		print("""\

  /\ 
 /  \ 
/    \ 
| __ | 
|_||_| 
 home
	""")



	def mapCastle():

		print("""
		___  ___  ___ 
		| |__| |__| | 
		|           | 
		| O  ___  O | 
		|  /     \  | 
		|__|_____|__| 
		   castle 
				""")

	def mapEmptyHorizontal():

		print("""
    _
    _""")



	def mapFilledHorizontal(key):

		mapFilledHorizontal = """
	_
	""""{}".format(key)
		print (mapFilledHorizontal)




	# | |__________             # ______________| |
	# |	 ___B______C|			# _____C____M_____|
	# |M|						#
								#







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

	empties = 0
	bosses = 0
	chests = 0
	monsters = 0
	hItems = 0

	#bossPlaced = 0
	iterate = int(generated.levels)
	while iterate > 0:
		for lev in range(0, iterate):					# replace array with random entities
			pick = random.randint(1, 6)
			if pick == 1:
				level.append("E")
				empties = empties + 1
				iterate = iterate - 1
			#if pick == 2 and bossPlaced == 0:           # originally set for one boss per level
			if pick == 2:
				level.append("B")
				#bossPlaced = 1
				bosses = bosses + 1
				iterate = iterate - 1
			if pick == 3:
				level.append("C")
				chests = chests + 1
				iterate = iterate - 1
			if pick == 4:
				level.append("M")
				monsters = monsters + 1
				iterate = iterate - 1
			if pick == 5:
				level.append("H")
				hItems = hItems + 1
				iterate = iterate - 1

	print("World Generated: \n{}".format(level))
	print("")
	print("Levels: {}, Empties: {}, Bosses: {}, Chests: {}, Monsters: {}, Hidden Items: {}".format(generated.levels, empties, bosses, chests, monsters, hItems))
	print("")
	print("")
	regen = input("Regenerate? (y/n)")
	print("")
	if regen == "y":
		game.Setup()
