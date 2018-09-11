import random
import characters
import time
import string


class BattlePrep():
	def __init__(self):	# take int for total enemies
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


class BattleSetup(BattlePrep):
	def __init__(self, player, total):
		print("You hear something coming closer...")
		print("")
		super(BattleSetup, self).__init__()
		self.player = player
		enemyCount = 0
		
		enemyName = random.choice(characters.GenerateEnemyList())			# need better way to do this >.<
		enemyString = "{}".format(enemyName)
		enemyNamed = enemyString[19:]
		enemyFinal = enemyNamed.strip("'>")

		enemy = enemyName(random.choice([True, False]), random.choice([True, False]), "{}".format(enemyFinal),random.randint(1,10),random.randint(1,99), random.randint(0,1), random.randint(0,400), random.randint(0,1))
		print("")
		print ("{} Appeared!!!".format(enemyFinal))
		print("")


		while enemy.health > 0:
			print("")
			print("[ e:Attack | s:Retreat \n"
			"[ i:Inventory | p:Player Info \n"
			"[v:Assess Enemy]")
			print("")
			answer = input(">>> ")
			if answer == "e":
				print("")
				print("You Attacked {}".format(enemyFinal))
				print("")
				player.attacks(player, enemy)
				print("")
				print("{} health damaged to  {}".format(enemyFinal, enemy.health))
			if answer == "p":
				print("")
				player.card()
			if answer == "v":
				enemy.avatar()


