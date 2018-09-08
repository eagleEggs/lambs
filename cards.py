

class GetCard():
	def __init__(self, character):
		self.character = character
		
	def card(character, specialOne, specialTwo):

		print("#######################")
		print("## Name: {}            ##".format(character.name))
		print("## Level: {}           ##".format(character.level))
		print("## Health: {}          ##".format(character.health))
		print("## Fatigue: {}         ##".format(character.fatigue))
		print("## Magic: {}           ##".format(character.magic))
		print("## Special One: {}     ##".format(specialOne))
		print("## Special Two: {}     ##".format(specialTwo))
		print("#######################")