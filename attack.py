class ClassicAttack():
	def __init__(self, attackName, damage, manaCost):
		self.attackName = attackName
		self.damage = damage
		self.manaCost = manaCost

	# Get Values
	def getName(self):
		return self.attackName
	def getDamage(self):
		return self.damage
	def getManaCost(self):
		return self.manaCost