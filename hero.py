# Variables
reset = '\033[0m'

# Classic Hero Class
class ClassicHero():
	# Initialize
	def __init__(self, name, health, maxHealth, mana, maxMana, defaultAttack, attackOne, attackTwo):
		self.name = name
		# Stats
		self.health = health
		self.maxHealth = maxHealth
		self.mana = mana
		self.maxMana = maxMana
		# Currency
		self.coins = 0
		self.gems = 0
		# Settings
		self.autoSave = 0
		# Attacks
		self.defaultAttack = defaultAttack
		self.attackOne = attackOne
		self.attackTwo = attackTwo
		# Leveling
		self.upgradeTokens = 0
		self.prestige = 0
		self.lvl = 1
		self.xp = 0
		# Boosts
		self.coinBoost = 0
		self.gemBoost = 0
		# Bank
		self.bankAccount = 0
		self.bankCoins = 0
		self.bankInterestRate = 1
	
	# Calculate
	def calcMaxXp(self):
		self.maxXp = (5 * self.lvl) ** 2

	# Stats
	def getName(self):
		return self.name
	def getHealth(self):
		return self.health
	def getMaxHealth(self):
		return self.maxHealth
	def getMana(self):
		return self.mana
	def getMaxMana(self):
		return self.maxMana
	# Currency
	def getCoins(self):
		return self.coins
	def getGems(self):
		return self.gems
	# Leveling
	def getLevel(self):
		return self.lvl
	def getXp(self):
		return self.xp
	def getMaxXp(self):
		return self.maxXp
	def getPrestige(self):
		return self.prestige
	def getUpgradeTokens(self):
		return self.upgradeTokens
	# Bank
	def getBankCoins(self):
		return self.bankCoins
	def getBankInterest(self):
		return self.bankInterestRate
	# Settings
	def calcAutoSave(self):
		if self.autoSave == 0:
			print("Auto Save: Off")
		elif self.autoSave == 1:
			print("Auto Save: On")

	# Heal
	def healHealth(self,x):
		self.health += x
		if self.health > self.maxHealth:
			self.health = self.maxHealth
	
	def healMana(self,x):
		self.mana += x
		if self.mana > self.maxMana:
			self.mana = self.maxMana

	def healAll(self):
		self.health = (self.health + (self.maxHealth - self.health))
		self.mana = (self.mana + (self.maxMana - self.mana))

	# XP and Leveling
	def gainXp(self,x):
		while True:
			self.calcMaxXp()
			# Gained Xp Less Than Max Xp
			if (self.xp + x) < self.maxXp:
				if self.lvl < 100:
					self.xp += x
					break
				elif self.lvl == 100:
					self.lvl -= 99
					self.prestige += 1
					self.upgradeTokens += 5
					print("Prestige {}!".format(self.getPrestige()))
					print("You Received 5 Upgrade Tokens!")
			# Gained Xp More Than Max Xp
			elif (self.xp + x) >= self.maxXp:
				xpLeftTillMax = self.maxXp - self.xp
				x -= xpLeftTillMax
				self.xp += xpLeftTillMax
				self.xp -= self.maxXp
				self.lvl += 1
				print("{} Leveled up to Level {}!".format(self.getName(),self.getLevel()))
				if self.lvl % 5 == 0:
					self.upgradeTokens += 1
					print("You Received an Upgrade Token!")

# Story Hero Class
class StoryHero():
	# Initialize
	def __init__(self,name,nationality,gender):
		self.name = name
		self.nationality = nationality
		self.gender = gender
		self.prologue = 1
		self.chapter = 1
		self.decisionNumber = 1
		self.tColor = '\033[0m'
		self.color = '\033[0m'

	# Get Values
	def getName(self):
		return self.name
	def getNationality(self):
		return self.nationality
	def getGender(self):
		return self.gender
	def getTColor(self):
		if self.tColor == '\033[0m':
			print("{}White{}".format(self.tColor,reset))
		if self.tColor == '\033[31m':
			print("{}Red{}".format(self.tColor,reset))
		if self.tColor == '\033[33m':
			print("{}Orange{}".format(self.tColor,reset))
		if self.tColor == '\033[36m':
			print("{}Blue{}".format(self.tColor,reset))
		if self.tColor == '\033[32m':
			print("{}Green{}".format(self.tColor,reset))
		if self.tColor == '\033[35m':
			print("{}Purple{}".format(self.tColor,reset))
	def getColor(self):
		if self.color == '\033[0m':
			print("{}White{}".format(self.color,reset))
		if self.color == '\033[31m':
			print("{}Red{}".format(self.color,reset))
		if self.color == '\033[33m':
			print("{}Orange{}".format(self.color,reset))
		if self.color == '\033[36m':
			print("{}Blue{}".format(self.color,reset))
		if self.color == '\033[32m':
			print("{}Green{}".format(self.color,reset))
		if self.color == '\033[35m':
			print("{}Purple{}".format(self.color,reset))

	# Functions
	def changeName(self,x):
		self.name = x
	def changeNationality(self,x):
		self.nationality = x
	def changeGender(self,x):
		self.gender = x
	def changeTitleColor(self,x):
		if x.lower() == "white":
			self.tColor = '\033[0m'
		if x.lower() == "red":
			self.tColor = '\033[31m'
		if x.lower() == "orange":
			self.tColor = '\033[33m'
		if x.lower() == "blue":
			self.tColor = '\033[36m'
		if x.lower() == "green":
			self.tColor = '\033[32m'
		if x.lower() == "purple":
			self.tColor = '\033[35m'
	def changeTextColor(self,x):
		if x.lower() == "white":
			self.color = '\033[0m'
		if x.lower() == "red":
			self.color = '\033[31m'
		if x.lower() == "orange":
			self.color = '\033[33m'
		if x.lower() == "blue":
			self.color = '\033[36m'
		if x.lower() == "green":
			self.color = '\033[32m'
		if x.lower() == "purple":
			self.color = '\033[35m'

	# Settings
	def calcAutoSave(self):
		if self.autoSave == 0:
			print("Auto Save: Off")
		elif self.autoSave == 1:
			print("Auto Save: On")