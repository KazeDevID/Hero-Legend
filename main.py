### IMPORTS ###
import pickle, random, os, sys, threading
from attack import *
from enemy import *
from hero import *
from replit import clear
from time import sleep

### Functions ###
def tprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.05)

### MODE SELECTION ###
def selectMode():
	while True:
		clear()
		print("Hero Legends - Mode Selection\n")
		print("[Modes]")
		print("(1) Classic Mode")
		print("(2) Story Mode [WIP]")
		selectedMode = input("\n> ")
		if selectedMode == "1":
			classicMenu()
		if selectedMode == "2":
			storyMenu()

### CLASSIC - VARIABLES ###
# Player Attacks
melee = ClassicAttack("Melee",20,0)
snowball = ClassicAttack("Snowball",30,10)
fireball = ClassicAttack("Fireball",40,15)
spear = ClassicAttack("Spear",30,10)
sword = ClassicAttack("Sword",40,15)
bowArrow = ClassicAttack("Bow & Arrow",30,10)
crossbow = ClassicAttack("Cross Bow",40,15)
# Monster / Boss Attacks
meleeEnemy = ClassicAttack("Melee",8,0)
meleeBoss = ClassicAttack("Melee",16,0)

# Players
wizard = ClassicHero("Wizard",125,125,125,125,melee,snowball,fireball)
knight = ClassicHero("Knight",175,175,75,75,melee,spear,sword)
archer = ClassicHero("Archer",150,150,100,100,melee,bowArrow,crossbow)

# Monsters & Bosses
monsterOne = ClassicEnemy("Monster",50,50,meleeEnemy)
monsterTwo = ClassicEnemy("Monster",75,75,meleeEnemy)
bossOne = ClassicEnemy("Boss",125,125,meleeBoss)
bossTwo = ClassicEnemy("Boss",150,150,meleeBoss)

# Monster / Boss Lists
monsterList = [monsterOne,monsterTwo]
bossList = [bossOne,bossTwo]

# Extra
guestAccess = 0

### CLASSIC - GET VALUES ###
def classicCharacterStats():
	print("[{}]".format(player.getName()))
	print("HP: ({}/{})".format(player.getHealth(),player.getMaxHealth()))
	print("Mana: ({}/{})\n".format(player.getMana(),player.getMaxMana()))

def classicDisplayAttack(x,y,z):
	print("\n({}) {} Attack [{}]".format(z,y,x.getName()))
	print("Damage: {}".format(x.getDamage()))
	if x.manaCost > 0:
		print("Mana Cost: {}".format(x.getManaCost()))

### CLASSIC - Bank Interest: Threading ###
def bankInterest():
	sleep(600)
	player.bankCoins = player.bankCoins * player.bankInterestRate
	threading.Timer(1, bankInterest).start()

### CLASSIC - MAIN MENU ###
def classicMenu():
	global guestAccess
	while True:
		clear()
		print("Hero Legends - Classic Mode")
		print("Important: Fork Game (Unless Playing as Guest!) to Save / Load Progress!")
		print("\n[Options]")
		print("(a) Mode Selection")
		print("\n[Main Menu]")
		print("(1) Tutorial")
		print("(2) Signup")
		print("(3) Login")
		print("(4) Guest")
		print("(5) Credits")
		menuInput = input("\n> ")
		if menuInput.lower() == "a":
			selectMode()
		elif menuInput == "1":
			classicTutorial()
		elif menuInput == "2":
			classicSignup()
		elif menuInput == "3":
			classicLogin()
		elif menuInput == "4":
			guest()
			guestAccess = 1
			classicPregame()
		elif menuInput == "5":
			credits()

### CLASSIC - TUTORIAL ###
def classicTutorial():
	while True:
		clear()
		print("Hero Legends - Tutorial\n")
		print("[Tutorial]")
		print("In Hero Legends, heroes fight monsters and bosses to level up and prestige.")
		print("Once they hit level 100, they prestige and gain stat boosts.")
		print("Every 5 levels, you will receive an upgrade token to use at the upgrade table.")
		print("You can boost your attack, defense and also the coins and gems you get from chests.")
		print("\n[Options]")
		print("(1) Main Menu")
		tutorialInput = input("\n> ")
		if tutorialInput == "1":
			classicMenu()

### CLASSIC - SIGNUP ###
def classicSignup():
	global username, password, filename
	clear()
	print("Hero Legends - Signup\n")
	print("[Signup]")
	username = input("Username: ")
	password = input("Password: ")
	filename = ("{}_{}Classic.pickle".format(username,password))
	if os.path.exists(filename):
		print("\nAccount Already Exists!")
		sleep(0.75)
		classicMenu()
	guestAccess = 0
	classicPregame()

### CLASSIC - LOGIN ###
def classicLogin():
	global username, password, filename
	clear()
	print("Hero Legends - Login\n")
	print("[Login]")
	username = input("Username: ")
	password = input("Password: ")
	filename = ("{}_{}Classic.pickle".format(username,password))
	if os.path.exists(filename):
		guestAccess = 0
		load()
		threading.Thread(target=bankInterest).start()
		classicGameMenu()
	else:
		print("\nAccount Does Not Exist!")
		sleep(0.75)
		classicMenu()

### CLASSIC - SAVE ###
def classicSave():
	if player.autoSave == 1:
		if os.path.exists(filename):
			os.remove(filename)
		with open(filename,'wb+') as f:
			pickle.dump(player,f)

### CLASSIC - LOAD ###
def classicLoad():
	global player
	with open(filename,'rb') as f:
		player = pickle.load(f)

### CLASSIC - PRE GAME ###
def classicPregame():
	global player
	while True:
		clear()
		print("Hero Legends - Select Character\n")
		print("(1) Wizard \nStats: HP:{}, Mana:{}".format(wizard.getHealth(),wizard.getMana()))
		print("(2) Knight \nStats: HP:{}, Mana:{}".format(knight.getHealth(),knight.getMana()))
		print("(3) Archer \nStats: HP:{}, Mana:{}\n".format(archer.getHealth(),archer.getMana()))
		characterInput = input("> ")
		if characterInput == "1":
			player = wizard
			break
		elif characterInput == "2":
			player = knight
			break
		elif characterInput == "3":
			player = archer
			break
	if guestAccess == 1:
		threading.Thread(target=bankInterest).start()
		classicGameMenu()
	# Settings
	while True:
		clear()
		player.calcAutoSave()
		print("Toggle AutoSave: (On/Off)")
		autoDetect = input("> ")
		if autoDetect.lower() == "on":
			player.autoSave = 1
			break
		elif autoDetect.lower() == "off":
			player.autoSave = 0
			break
	classicSave()
	threading.Thread(target=bankInterest).start()
	classicGameMenu()

### CLASSIC - GAME MENU ###
def classicGameMenu():
	while True:
		player.calcMaxXp()
		clear()
		print("Hero Legends - Game Menu\n")
		print("[{}]".format(username))
		print("Coins: {}".format(player.getCoins()))
		print("Gems: {}\n".format(player.getGems()))
		classicCharacterStats()
		print("Level: {}".format(player.getLevel()))
		print("XP: ({}/{})".format(player.getXp(), player.getMaxXp()))
		print("\n[Game Menu]")
		print("(a) Play Level")
		print("(b) Upgrade Table")
		print("(c) Shop")
		print("(d) Casino")
		print("(e) Bank")
		print("\n[Options]")
		print("(1) Save")
		print("(2) Settings")
		print("(3) Exit")
		gameInput = input("\n> ")
		if gameInput.lower() == "a":
			classicChooseLevel()
		elif gameInput.lower() == "b":
			classicUpgradeTable()
		elif gameInput.lower() == "c":
			classicShop()
		elif gameInput.lower() == "d":
			classicCasino()
		elif gameInput.lower() == "e":
			classicBank()
		elif gameInput == "1":
			classicSave()
		elif gameInput == "2":
			classicSettings()
		elif gameInput == "3":
			if player.autoSave == 1:
				classicSave()
			sys.exit(0)

### CLASSIC - LEVEL ###
def classicChooseLevel():
	global monsterCount, bossCount, chestMonsterCount,chestBossCount
	clear()
	# Choose Number of Monsters and Bosses
	monsterCount = random.randrange(2,6)
	bossCount = random.randrange(1,3)
	chestMonsterCount = monsterCount
	chestBossCount = bossCount
	# Play Level
	while True:
		if monsterCount > 0 or bossCount > 0:
			classicPlayLevel()
		elif monsterCount == 0 and bossCount == 0:
			player.healAll()
			classicChest()
			break

# Play Level
def classicPlayLevel():
	global chosenAttackWeapon, pickedMonster, currentEnemy, monsterCount, bossCount
	# Pick Monster
	if monsterCount > 0:
		pickedMonster = random.choice(monsterList)
		currentEnemy = "monster"
	# Pick Boss
	elif monsterCount == 0 and bossCount > 0:
		pickedMonster = random.choice(bossList)
		currentEnemy = "boss"
	# Loop Attacking
	while True:
		clear()
		classicLevelCheck()
		# Monster Dead
		if pickedMonster.health <= 0:
			print("Hero Legends\n")
			print("You defeated a {}".format(pickedMonster.getName()))
			# Player Xp
			if pickedMonster.name == "Monster":
				xpCount = (player.lvl * 5)
			elif pickedMonster.name == "Boss":
				xpCount = (player.lvl * 10)
			player.gainXp(xpCount)
			print("You got {} Xp!".format(xpCount))
			input("\nPress 'Enter' to Continue!")
			clear()
			pickedMonster.healAll()
			if currentEnemy == "monster":
				monsterCount -= 1
				break
			if currentEnemy == "boss":
				bossCount -= 1
				break
		# Fighting Monsters / Bosses
		print("Hero Legends - Level\n")
		print("[Enemies]")
		if monsterCount > 0:
			print("Monsters: {}".format(monsterCount))
		print("Bosses: {}\n".format(bossCount))
		classicCharacterStats()
		print("[Enemy]")
		print("{}".format(pickedMonster.getName()))
		print("HP: ({}/{})\n".format(pickedMonster.health,pickedMonster.maxHealth))
		print("[Attack]")
		classicDisplayAttack(player.defaultAttack,"Default","a")
		classicDisplayAttack(player.attackOne,"Primary","b")
		classicDisplayAttack(player.attackTwo,"Secondary","c")
		print("\n[Options]")
		print("(1) Run Away")
		attackInput = input("\n> ")
		if attackInput.lower() == "a":
			chosenAttackWeapon = player.defaultAttack
			classicAttackDamage()
		elif attackInput.lower() == "b":
			chosenAttackWeapon = player.attackOne
			classicAttackDamage()
		elif attackInput.lower() == "c":
			chosenAttackWeapon = player.attackTwo
			classicAttackDamage()
		elif attackInput.lower() == "1":
			runawayChance = random.randint(0,101)
			if runawayChance < 25:
				player.healAll()
				pickedMonster.healAll()
				print("\nYou Successfully Ranaway!")
				sleep(1.5)
				classicGameMenu()
			else:
				print("\nYou Were Unsuccessful in Running Away!")
				sleep(1)
				classicEnemyAttackDamage()

# Level Check
def classicLevelCheck():
	# Player Dead
	if player.health <= 0:
		player.healAll()
		print("Hero Legends\n")
		print("[Stats]")
		print("You Died!")
		randomCoins = random.randint(5,11)
		if player.coins >= randomCoins:
			player.coins -= randomCoins
		else:
			randomCoins = player.coins
			player.coins -= randomCoins
		if randomCoins > 0:
			print("You Lost {} Coins!".format(randomCoins))
		input("\nPress 'Enter' to Return to Hub!")
		classicGameMenu()

# Enemy Attack
def classicEnemyAttackDamage():
	if pickedMonster.health > 0:
		enemyHitChance = random.randint(0,101)
		if enemyHitChance < 75:
			doDamage = random.randint(4,pickedMonster.attackOne.damage)
			player.health -= doDamage
			print("{} did {} Damage to your {}".format(pickedMonster.getName(),doDamage,player.getName()))
		else:
			print("\n{} Missed Attack".format(pickedMonster.getName()))
		sleep(1)
		clear()

# Player vs. Enemy
def classicAttackDamage():
	# Player Attacks Enemy
	if player.mana >= chosenAttackWeapon.manaCost:
		pickedMonster.health -= chosenAttackWeapon.damage
		player.mana -= chosenAttackWeapon.manaCost
		print("\n{} used {} and did {} Damage to the {}".format(player.getName(),chosenAttackWeapon.getName(),chosenAttackWeapon.getDamage(),pickedMonster.getName()))
		sleep(1)
		if chosenAttackWeapon.manaCost > 0:
			print("Mana Lost: {}".format(chosenAttackWeapon.getManaCost()))
			sleep(1.5)
		# Enemy Hits Player
		classicEnemyAttackDamage()
	else:
		print("\nNot Enough Mana!")
		sleep(1)
		clear()

# Chest
def classicChest():
	chestGems = 0
	# Randomize
	chestMonsterCoins = random.randint(chestMonsterCount, (5*chestMonsterCount))
	chestBossCoins = random.randint(chestBossCount, (10*chestBossCount))
	chestGemsChance = random.randint(0,101)
	# Amounts
	totalChestCoins = chestMonsterCoins + chestBossCoins + player.coinBoost
	player.coins += totalChestCoins
	if chestGemsChance < 10 + player.gemBoost:
		chestGems = 1
		player.gems += chestGems
	clear()
	print("Hero Legends\n")
	print("[Items]")
	print("Coins Earned: {}".format(totalChestCoins))
	if chestGems > 0:
		print("Gems Earned: {}".format(chestGems))
	input("\nPress 'Enter' to Close Chest!")
	if player.autoSave == 1:
		classicSave()

### CLASSIC - UPGRADE TABLE ###
def classicUpgradeTable():
	while True:
		clear()
		print("Hero Legends- Upgrade Table")
		print("Upgrade Tokens: {}".format(player.getUpgradeTokens()))
		print("\n[Upgrade Table]")
		print("(a) Health Cap [+20]")
		print("(b) Mana Cap [+20]")
		print("(c) Chest Coin Boost [+2]")
		print("(d) Chest Gem Boost [+1%]\n")
		print("[Options]")
		print("(1) Game Menu")
		upgradeTableInput = input("\n> ")
		if upgradeTableInput == "1":
			classicGameMenu()
		if player.upgradeTokens > 0:
			player.upgradeTokens -= 1
			if upgradeTableInput == "a":
				player.maxHealth += 20
				player.healAll()
				print("\nSuccessfully Upgraded Health Cap by 20")
			elif upgradeTableInput == "b":
				player.maxMana += 20
				player.healAll()
				print("\nSuccessfully Upgraded Mana Cap by 20")
			elif upgradeTableInput == "c":
				player.coinBoost += 2
				print("\nSuccessfully Upgraded Coin Boost by 2")
			elif upgradeTableInput == "d":
				player.gemBoost += 1
				print("\nSuccessfully Upgraded Gem Boost by 1%")
			if player.autoSave == 1:
				classicSave()
		else:
			print("\nNot Enough Upgrade Tokens!")
		input("Press 'Enter' to Continue!")

### CLASSIC - SHOP ###
def classicShop():
	while True:
		clear()
		print("Hero Legends- Shop\n")
		print("[Shop]")
		print("\n[Menu]")
		print("(1) Game Menu")
		shopInput = input("\n> ")
		if shopInput == "1":
			classicGameMenu()

### CLASSIC - CASINO ###
def classicCasino():
	while True:
		clear()
		print("Hero Legends - Casino")
		print("Coins: {}".format(player.getCoins()))
		print("\n[Gamble]")
		print("(a) Slots")
		print("\n[Options]")
		print("(1) Game Menu")
		print("(2) Gamble Info")
		gambleInput = input("\n> ")
		# Slots
		if gambleInput.lower() == "a":
			classicSlots()
		if gambleInput == "1":
			classicGameMenu()
		if gambleInput == "2":
			classicSlotsInfo()

def classicSlots():
	try:
		slotsAmount = input("Gamble Amount: ")
		if int(slotsAmount) > 0 and player.coins >= int(slotsAmount):
			player.coins -= int(slotsAmount)
			numberOne = random.randint(0,5)
			numberTwo = random.randint(0,5)
			numberThree = random.randint(0,5)
			clear()
			print("| {} | {} | {} |".format(numberOne,numberTwo,numberThree))
			# 3x Money | 3 Numbers
			if numberOne == numberTwo and numberOne == numberThree:
				sleep(1)
				print("You matched 3 numbers!")
				print("You have won 3x your gambled money: ${}!".format(3*int(slotsAmount)))
				player.coins += (3*int(slotsAmount))
				sleep(2.5)
			# 2x Money | 2 Numbers
			elif numberOne == numberTwo or numberTwo == numberThree or numberOne == numberThree:
				sleep(1)
				print("You matched 2 numbers!")
				print("You have won 2x your gambled money: ${}!".format(2*int(slotsAmount)))
				player.coins += (2*int(slotsAmount))
				sleep(2.5)
			# 0x Money | 1 or 0 Numbers
			else:
				sleep(1)
				print("You matched 0 numbers!")
				print("You lost all your gambled money!")
				sleep(2.5)
	except:
		clear()

def classicSlotsInfo():
	clear()
	print("[Slots]")
	print("Three numbers are rolled from 1 to 5.")
	print("No numbers matched = lose gambled money")
	print("Two numbers matched = 2x gambled money")
	print("Three numbers matched = 3x gambled money")
	input("\nPress 'Enter' to continue!")

### CLASSIC - BANK ###
def classicBank():
	while True:
		if player.bankAccount == 0:
			classicCreateBankAccount()
		clear()
		print("Hero Legends - Bank\n")
		print("Coins: {}".format(player.getCoins()))
		print("Bank Balance: {}".format(int(player.getBankCoins())))
		print("\n[Bank]")
		print("(a) Deposit")
		print("(b) Withdraw")
		print("\n[Options]")
		print("(1) Game Hub")
		bankInput = input("\n> ")
		if bankInput.lower() == "a":
			try:
				depositAmount = input("Deposit Amount: ")
				if int(depositAmount) > 0 and player.coins >= int(depositAmount):
					player.bankCoins += int(depositAmount)
					player.coins -= int(depositAmount)
					print("\nSuccessfully Deposited!")
					sleep(0.75)
				else:
					print("\nError!")
					sleep(0.75)
			except:
				print("\nError!")
				sleep(0.75)
		elif bankInput.lower() == "b":
			try:
				withdrawAmount = input("Withdraw Amount: ")
				if int(withdrawAmount) > 0 and player.bankCoins >= int(withdrawAmount):
					player.coins += int(withdrawAmount)
					player.bankCoins -= int(withdrawAmount)
					print("Successfully Withdrawn!")
					sleep(0.75)
				else:
					print("\nError!")
					sleep(0.75)
			except:
				print("\nError!")
				sleep(0.75)
		elif bankInput == "1":
			classicGameMenu()

def classicCreateBankAccount():
	while True:
		clear()
		print("Hero Legends - Bank\n")
		print("Coins: {}".format(player.getCoins()))
		print("Gems: {}\n".format(player.getGems()))
		print("[Bank Accounts]")
		print("(a) Basic Account [Interest: 2%] [Cost: 100 Coins & 5 Gems]")
		print("(b) Standard Account [Interest: 5%] [Cost: 250 Coins & 10 Gems]")
		print("(c) Premium Account [Interest: 10%] [Cost: 500 Coins & 20 Gems]")
		print("\n[Options]")
		print("(1) Game Menu")
		bankAccountChoice = input("\n> ")
		if bankAccountChoice.lower() == "a" and player.coins >= 100 and player.gems >= 5:
			print("\nSuccessful Purchase of Basic Account!")
			player.coins -= 100
			player.gems -= 5
			player.bankInterestRate += 0.02
			player.bankAccount += 1
			sleep(1.5)
			classicBank()
		elif bankAccountChoice.lower() == "b" and player.coins >= 250 and player.gems >= 10:
			print("\nSuccessful Purchase of Standard Account!")
			player.coins -= 250
			player.gems -= 10
			player.bankInterestRate += 0.05
			player.bankAccount += 1
			sleep(1.5)
			classicBank()
		elif bankAccountChoice.lower() == "c" and player.coins >= 500 and player.gems >= 20:
			print("\nSuccessful Purchase of Premium Account!")
			player.coins -= 500
			player.gems -= 20
			player.bankInterestRate += 0.1
			player.bankAccount += 1
			sleep(1.5)
			classicBank()
		elif bankAccountChoice == "1":
			classicGameMenu()
		else:
			print("\nError!")
			sleep(1.5)

### CLASSIC - SETTINGS ###
def classicSettings():
	while True:
		clear()
		print("Hero Legends - Settings\n")
		print("[Settings]")
		print("(a)", end = " ")
		player.calcAutoSave()
		print("\n[Settings Menu]")
		print("(1) Game Menu")
		settingsMenu = input("\n> ")
		if settingsMenu == "1":
			classicGameMenu()
		if settingsMenu.lower() == "a":
			classicToggleAutoSave()

# Toggle Auto Save
def classicToggleAutoSave():
	clear()
	player.calcAutoSave()
	print("Toggle Autosave: (On/Off)")
	changeAutoSave = input("> ")
	clear()
	if guestAccess == 1:
		print("Error!\nYou are using guest access!")
	elif changeAutoSave.lower() == "on" and player.autoSave == 0:
		player.autoSave += 1
		print("Turned on Auto Save!")
	elif changeAutoSave.lower() == "off" and player.autoSave == 1:
		player.autoSave -= 1
		print("Turned off Auto Save!")
	sleep(1)
	classicSave()

### STORY - VARIABLES ###
storyGuest = 0
# Player
storyPlayerTemplate = StoryHero("Name","Nationality","Gender")
# Color
reset = '\033[0m'
red = '\033[31m'
orange = '\033[33m'
blue = '\033[36m'
green = '\033[32m'
purple = '\033[35m'

### STORY - MAIN MENU ###
def storyMenu():
	global storyGuest
	while True:
		clear()
		print("Hero Legends - Story Mode\n")
		print("[Options]")
		print("(1) Mode Selection")
		print("\n[Main Menu]")
		print("(a) Signup")
		print("(b) Login")
		print("(c) Guest")
		print("(d) Credits")
		menuInput = input("\n> ")
		if menuInput == "1":
			selectMode()
		elif menuInput.lower() == "a":
			storySignup()
		elif menuInput.lower() == "b":
			storyLogin()
		elif menuInput.lower() == "c":
			storyGuest = 1
			guest()
			storyPregame()
		elif menuInput.lower() == "d":
			credits()

### STORY - SIGNUP ###
def storySignup():
	global username, password, filename
	clear()
	print("Hero Legends - Signup\n")
	print("[Signup]")
	username = input("Username: ")
	password = input("Password: ")
	filename = ("{}_{}Story.pickle".format(username,password))
	if os.path.exists(filename):
		print("\nAccount Already Exists!")
		sleep(0.75)
		storyMenu()
	guestAccess = 0
	storyPregame()

### STORY - LOGIN ###
def storyLogin():
	global username, password, filename
	clear()
	print("Hero Legends - Login\n")
	print("[Login]")
	username = input("Username: ")
	password = input("Password: ")
	filename = ("{}_{}Story.pickle".format(username,password))
	if os.path.exists(filename):
		guestAccess = 0
		storyLoad()
		storyGame()
	else:
		print("\nAccount Does Not Exist!")
		sleep(0.75)
		storyMenu()

### STORY - SAVE ###
def storySave():
	if storyGuest == 0:
		if os.path.exists(filename):
			os.remove(filename)
		with open(filename,'wb+') as f:
			pickle.dump(storyPlayer,f)

### STORY - LOAD ###
def storyLoad():
	global storyPlayer
	with open(filename,'rb') as f:
		storyPlayer = pickle.load(f)

### STORY - PREGAME ###
def storyPregame():
	global storyPlayer
	storyPlayer = storyPlayerTemplate
	storySave()
	storyGame()

### STORY - GAME ###
def storyGame():
	while True:
		# Prologue
		if storyPlayer.prologue == 1:
			storyInfo()
			clear()
			storyPrologue("repeat")
			while True:
				clear()
				storyPrologue("play")
				print("{}\nType 'Continue' to move on.{}".format(storyPlayer.color,reset))
				prologueInput = input("> ")
				if prologueInput.lower() == "settings":
					storySettings()
				elif prologueInput.lower() == "save":
					storySave()
				elif prologueInput.lower() == "exit":
					sys.exit(0)
				elif prologueInput.lower() == "help":
					storyInfo()
				elif prologueInput.lower() == "continue":
					storyPlayer.prologue -= 1
					break
		# Story Complete
		else:
			storyComplete()

### STORY - INFORMATION ###
def storyInfo():
	while True:
		clear()
		print("{}Hero Legends - Infomation{}\n".format(storyPlayer.tColor,reset))
		print("{}Type the following in story mode when it asks for an input.\n".format(storyPlayer.tColor))
		print("{}'Help' - Open This Help Menu".format(storyPlayer.color))
		print("'Save' - Save Progress [Not on Guest Mode]")
		print("'Settings' - Open Settings Menu{}".format(reset))
		print("\nType 'okay' to continue!")
		infoInput = input("> ")
		if infoInput.lower() == "okay":
			break
### STORY - PROLOGUE ###
def storyPrologue(x):
	# Prologue
	prologue = "Centuries ago, in the village of Xernia, full of lush gardens and forests with vibrant scenery, an army of horrific monsters came to raid this peaceful villages and claim Xernia as theirs. Three brave heroes stood up and casted extraordinary spells to seal off the horde of monsters inside a new dimension after breaching a portal in this reality. The villagers of Xernia were thankful for these heroes and without them, they would've lost their only home. They soon became part of the legend which was passed down for generations."
	print("{}Hero Legends - Prologue{}\n".format(storyPlayer.tColor,reset))
	sleep(0.5)
	if x.lower() == "play":
		print("{}{}{}".format(storyPlayer.color,prologue,reset))
	if x.lower() == "repeat":
		tprint("{}{}{}".format(storyPlayer.color,prologue,reset))

### STORY - COMPLETE ###
def storyComplete():
	while True:
		clear()
		print("{}Hero Legends - Complete\n".format(storyPlayer.tColor))
		print("[Victory]{}".format(storyPlayer.color))
		print("You Beat Story Mode!")
		print("Many more chapters coming soon!{}".format(reset))
		input("\n> ")

### STORY - SETTINGS ###
def storySettings():
	while True:
		clear()
		print("{}Hero Legends - Settings\n".format(storyPlayer.tColor))
		print("[Settings]{}".format(storyPlayer.color))
		print("(a) Color")
		print("\n{}[Options]{}".format(storyPlayer.tColor,storyPlayer.color))
		print("(1) Exit{}".format(reset))
		settingsMenu = input("\n> ")
		if settingsMenu == "1":
			break
		elif settingsMenu.lower() == "a":
			storyToggleColor()

# Toggle Color Change
def storyToggleColor():
	while True:
		clear()
		print("Title Color: ", end = '')
		storyPlayer.getTColor()
		print("Text Color: ", end = '')
		storyPlayer.getColor()
		print("\n{}[Color Options - Type]{}".format(storyPlayer.tColor,reset))
		print("White")
		print("{}Red".format(red))
		print("{}Orange".format(orange))
		print("{}Blue".format(blue))
		print("{}Green".format(green))
		print("{}Purple".format(purple))
		print("\n{}[Options]{}".format(storyPlayer.tColor,reset))
		print("(1) Exit")
		colorInput = input("\n> ")
		if colorInput == "1":
			break
		if colorInput.lower() in ("white", "red", "orange", "blue", "green", "purple", "yellow"):
			print("\nChoose [Title/Text]")
			colorPlaceInput = input("> ")
			if colorPlaceInput.lower() == "title":
				storyPlayer.changeTitleColor(colorInput)
			if colorPlaceInput.lower() == "text":
				storyPlayer.changeTextColor(colorInput)

### SIMILAR FUNCTIONS - GUEST ###
def guest():
	global username
	clear()
	print("Hero Legends - Guest\n")
	print("[Guest]")
	username = input("Username: ")

### SIMILAR FUNCTIONS - CREDITS ###
def credits():
	clear()
	print("Hero Legends - Credits\n")
	print("[Game Makers]")
	print("(Programmer) KazeDevID")
	print("\n[Socials]")
	print("Whatsapp - 081342399968")
	print("YouTube - KAZEDEVID")
	print("TikTok - @punyakaze91")
	print("SnackVideo - kuira360")
	print("Telegram - @KazeDevID")
	input("\nPress 'Enter' to continue!")

### RUN GAME ###
selectMode()