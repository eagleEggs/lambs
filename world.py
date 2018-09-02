class World():

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