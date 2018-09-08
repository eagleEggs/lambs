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
	enemy = characters.Vampire(True, True, "Vampire",10,99, 0, 400, 1)
	print("")
	print ("It's a {}!!!".format(enemy.name))
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
			#player.cards.GetCard()
		if answer == "v":
			enemy.card()