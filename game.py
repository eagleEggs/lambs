import time
import random
from colorama import init, Fore, Back, Style
import characters



def battleSuspense():

	begin = 1
	end = random.randint(2,10)
	suspense = range(begin, end)
	timeString = '.'*end
	print (timeString)
	for i in suspense:
		time.sleep(0.5)
		end = end-1
		timeString = '.'*end
		print(timeString)


def BattleMode(player):
	print("You hear something coming closer...")
	print("")
	battleSuspense()
	enemy = characters.Vampire(1,1,"Vampire",10,99, 0, 400)
	print("")
	print (Fore.RED + "It's a {}!!!".format(enemy.name))
	print("")
	#generate random enemy
	BattleEpic(enemy, player)


def BattleEpic(enemy, player):

	while enemy.health > 0:
		
		# turn based

		print("What are you going to do?")
		print("")
		print("[ e:Attack | s:Retreat \n"
			"[ i:Inventory | p:Player Info \n"
			"[v:Assess Enemy]")
		print("")
		answer = input(">>> ")
		if answer == "e":
			print("")
			print("You Attacked {}".format(enemy.name))
			print("")
			player.attacks(player, enemy)
			print("")
			print("{} health damaged to  {}".format(enemy.name, enemy.health))
		if answer == "p":
			print("")
			print(player)
		if answer == "v":
			print(enemy)



def introStory():
	inputName = input("Enter Your Name Adventurer: ")
	player = characters.Warrior("plunger", "{}".format(inputName), 100, 100, 0, 100)
	#print(player.weapon.damage)
	print("")
	inputSize = input("Choose your map size:")
	mapSize = inputSize
	print("")

	print("You begin your adventure {}, \nupon waking amidst the showing rain of the darkest forest...".format(inputName))
	print("")
	input("Press Enter to Get up from your long sleep...")
	print("")

	BattleMode(player)

###############
#### GAME #####
###############

if __name__ == '__main__':

	# load map options

	# display current map info

	# ask for paths to take
	init(autoreset=True)
	introStory()

	# loop

	#inputName = input("Enter Your Name Adventurer: ")
	#player = Warrior("plunger", "{}".format(inputName), 100, 100, 0, 100)

	#print("You begin your adventure {}, upon waking amidst the showing rain of the darkest forest...".format(inputName))
	#input("Press Enter to Get up from your long sleep...")

	#print("You hear something coming closer...")
	#battleSuspense()
	#enemy = Vampire(1,1,"Vampire",200,99, 0, 400)
	#print ("It's a {}!!!".format(enemy.name))
	#print("What are you going to do?")
	#print("[ e:Attack | s:Retreat \n"
	#"[ i:Inventory | p:Player Info")
	#answer = input(">>> ")
	#if answer == "e":
	#	print("You Attacked {}".format(enemy.name))
	#	player.attacks(enemy)
	#if answer == "p":
	#	print(player)





###############
### Testing ###
###############

#vampireEnemy = Vampire(1,1,"Alucard",200,99, 0, 400)
#vampireEnemy.fly()




#print(vampireEnemy.health)
#vampireEnemy.attacks(vampireEnemy)
#print(vampireEnemy.health)
#blobEnemy = Blob(0,0,100,10,0,100, "Blobbly")
#blobEnemy.duplicate(4)
#blobDupe = blobEnemy
#print(blobEnemy.health)
#print(blobDupe.health)
#player = Warrior("stick", "StrongMan", 100,0,200, 99)
#print(player.name)
#print(player.health)
#player.attacks(player)
#print(player.health)
#world = World("forest")
#print(world)


