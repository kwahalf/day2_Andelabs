class Car(object):
	def __init__(self, name= "General",  model = "GM", Type = None):
		self.name = name
		self.model = model
		self.Type = Type
		self.speed = 0
		if (self.name == "Porshe" or self.name == "Koenigsegg"):
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4
		if self.Type == "trailer":
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4
	def is_saloon(self):
		if self.Type is not "trailer":
			self.Type == "saloon"
			return True
		return False
	def drive(self, moving_speed):
		if moving_speed == 3:
			self.speed = 1000
		elif moving_speed == 7:
			self.speed =77
		return self 



