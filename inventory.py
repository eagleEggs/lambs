


class Inventory():
	def __init__(self, slots=3):
		self.slots = slots

		@property
		def slots(self):
			return self._slots



class FannyPack(Inventory):
	def __init(self, fannySlots=1):
		self.slots = slots
		super(FannyPack, self).__init__(*args)



class Rings(Inventory):
	def __init__(self, ring, index, pinky):
		self.ring = ring
		self.index = index
		self.pinky = pinky
		super(Rings, self).__init__(*args)


class StorageBox():
	def __init__(self, boxSlots=10):
		self.boxSlots = boxSlots
		super(StorageBox, self).__init__(*args)




#################
#### Testing ####
#################


newInventory = Inventory()
print(newInventory.slots)


