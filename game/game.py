import time
import random
import characters
import world
import logo
import inventory
import battle


def introStory(player):
	print("You begin your adventure {}, \nupon waking amidst the showing rain of the darkest forest...".format(player.name))
	print("")
	input("Press Enter to Get up from your long sleep...")
	print("")

	battle.BattleSetup(player, 3)


def Setup():
	print("")
	inputName = input("Enter Your Name Adventurer: ")
	print("")
	print("Choose your Class:")
	print("w | Warrior")
	print("")
	classChoice = input(">")
	if classChoice == "w":
		player = characters.Warrior("plunger", "{}".format(inputName), 100, 100, 0, 100, 1)
	print("")

	worldType = input("Auto Generate [a], or Manual World Generation [m]?")
	print("")
	if worldType == "a":
		generatedWorld = world.worldGen("auto", random.randint(1,99),random.randint(1,99),random.randint(1,99),random.randint(1,99),random.randint(1,99),random.randint(1,99))
		print("")
	if worldType == "m":
		nLevels = input("Enter number of Levels: ")
		nEmpty = input("Enter number of Empty Levels :")
		nBosses = input("Enter number of Bosses: ")
		nChests = input("Enter number of Chests: ")
		nMonsters = input("Enter number of Monsters: ")
		nHiddenItems = input("Enter number of Hidden Items: ")
		
		generatedWorld = world.worldGen("manual", nLevels, nEmpty, nBosses, nChests, nMonsters, nHiddenItems)
		print("")

	introStory(player)


###############
#### GAME #####
###############

if __name__ == '__main__':

	Setup()
