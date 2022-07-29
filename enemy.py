class ClassicEnemy():
	def __init__(self, name, health, maxHealth, attackOne):
		self.name = name
		# Stats
		self.health = health
		self.maxHealth = maxHealth
		self.attackOne = attackOne

	# Get Values
	def getName(self):
		return self.name
	def getHealth(self):
		return self.health
	def getMaxHealth(self):
		return self.maxHealth

	# Heal
	def healAll(self):
		self.health = (self.health + (self.maxHealth - self.health))