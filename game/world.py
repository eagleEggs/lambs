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

class worldGen(World):
	def __init__(self, worldType, *args):
		super(worldGen, self).__init__(*args)
		self.worldType = worldType

		level = []									# set up level array

		empties = 0
		bosses = 0
		chests = 0
		monsters = 0
		hItems = 0

		#bossPlaced = 0
		if self.worldType == "auto":
			iterate = int(self.levels)
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
			print("Levels: {}, Empties: {}, Bosses: {}, Chests: {}, Monsters: {}, Hidden Items: {}".format(self.levels, empties, bosses, chests, monsters, hItems))
			print("")
			print("")
			regen = input("Regenerate? (y/n)")
			print("")
			if regen == "y":
				worldGen("auto", random.randint(1,99), self.empty, self.bosses, self.chests, self.monsters, self.hiddenItems)

		if self.worldType == "manual":
			
			empties = int(self.empty)
			bosses = int(self.bosses)
			chests = int(self.chests)
			monsters = int(self.monsters)
			hItems = int(self.hiddenItems)

			iterate = int(self.levels)
			while iterate > 0:
				for lev in range(0, iterate):
					pick = random.randint(1, 6)
					if pick == 1 and empties != 0:
						level.append("E")
						empties = empties - 1
						iterate = iterate - 1
					if pick == 2 and bosses != 0:
						level.append("B")
						bosses = bosses - 1
						iterate = iterate - 1
					if pick == 3 and chests != 0:
						level.append("C")
						chests = chests - 1
						iterate = iterate - 1
					if pick == 4 and monsters != 0:
						level.append("M")
						monsters = monsters - 1
						iterate = iterate - 1
					if pick == 5 and hItems != 0:
						level.append("H")
						hItems = hItems - 1
						iterate = iterate - 1

			print("World Generated: \n{}".format(level))
			print("")
			print("Levels: {}, Empties: {}, Bosses: {}, Chests: {}, Monsters: {}, Hidden Items: {}".format(self.levels, empties, bosses, chests, monsters, hItems))
			print("")
			print("")
			regen = input("Redo? (y/n)")
			print("")
			if regen == "y":
				worldGen("manual", self.levels, self.empty, self.bosses, self.chests, self.monsters, self.hiddenItems)


		@property
		def levels(self):
			return self.__levels

	def __repr__(self):
		return "Levels: {}".format(self.levels)

	def __str__(self):
		return "Levels: {}".format(self.levels)


class WorldStep(World):
	def __init__(self, currentLevel, nextLevel):
		self.currentLevel = currentLevel
		self.nextLevel = nextLevel

	def progress(self):
		self.currentLevel = self.nextLevel



