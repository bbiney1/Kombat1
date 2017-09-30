import fileinput
import msvcrt
import os
import time

# Useful Functions
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def getch():
	key = ord(msvcrt.getch())
	return key

# Non-Gameplay
def startup():
	clear()

	global saveStatus
	saveStatus = None

	#print("In association with no one", end = "", flush = True)
	#time.sleep(1)
	#print(" .", end = "", flush = True)
	#time.sleep(0.5)
	#print(" .", end = "", flush = True)
	#time.sleep(0.5)
	#print(" .")
	#time.sleep(1)
	
	#clear()
	#print("'Games on a Train' presents", end = "", flush = True)
	#time.sleep(1)
	#print(" .", end = "", flush = True)
	#time.sleep(0.5)
	#print(" .", end = "", flush = True)
	#time.sleep(0.5)
	#print(" .")
	#time.sleep(1)

def mainMenu():
	clear()
	print("  //\   _    _ ___  ___ ___")
	print(" //  \  |\  /| |__| |__ |__|")
	print("//    \ | \/ | |__| |__ |  |")
	time.sleep(0.5)
	print("")
	print("1) New Game")
	time.sleep(0.25)
	print("2) Load Game")
	time.sleep(0.25)
	print("3) Bind Controls")
	time.sleep(0.25)
	print("4) Help")
	time.sleep(0.25)
	print("5) Credits")
	time.sleep(0.25)
	print("6) Quit")
	time.sleep(0.25)
	print("")
	print("Press 1, 2, 3, 4, 5, or 6")

	c = True
	while c == True:
		key = getch()
		
		# New Game
		if key == 49:
			c = False
			newGame()
		
		# Load Game
		elif key == 50:
			c = False
			pauseMenu()
		
		# Bind Controls
		elif key == 51:
			c = False
			if bindControls() == False:
				mainMenu()
		
		# Help
		elif key == 52:
			c = False
			print("SUCCESS 4")
		
		# Credits
		elif key == 53:
			c = False
			credits()

		# Quit
		elif key == 54:
			c = False
			if quitGame() == False:
				mainMenu()

def pauseMenu():
	clear()
	print("  //\   _    _ ___  ___ ___")
	print(" //  \  |\  /| |__| |__ |__|")
	print("//    \ | \/ | |__| |__ |  |")
	print("")
	print("Game is paused")
	time.sleep(0.25)
	print("")
	print("1) Save Game")
	time.sleep(0.25)
	print("2) Bind Controls")
	time.sleep(0.25)
	print("3) Help")
	time.sleep(0.25)
	print("4) Quit to Main Menu")
	time.sleep(0.25)
	print("5) Quit")
	time.sleep(0.25)
	print("")
	print("Press 'esc' again to unpause")

	c = True
	while c == True:
		key = getch()

		# Save Game
		if key == 49:
			c = False
			
			clear()
			#save()
			saveStatus = True
			print("Game saved!")
			time.sleep(1)
			pauseMenu()
		
		# Bind Controls
		if key == 50:
			c = False
			if bindControls() == False:
				pauseMenu()

		# Help
		if key == 51:
			c = False
			print("SUCCESS")

		# Quit to Menu
		if key == 52:
			c = False
			quitMenu()

		# Quit
		elif key == 53:
			c = False
			if quitGame() == False:
				pauseMenu()

def newGame():
	clear()
	print("Select a save slot:")
	print("")
	print("")

def bindControls():
	global controlsFileList
	with open('controls.txt', 'r') as controlsFile:
		controlsFileList = controlsFile.readlines()

	clear()
	print("To rebind a key press the number the action corresponds to.")
	print("")
	print("1) Test1: {}".format(controlsFileList[0]))
	print("2) Test2: {}".format(controlsFileList[1]))
	print("3) Test3: {}".format(controlsFileList[2]))
	print("4) Test4: {}".format(controlsFileList[3]))
	print("5) Test5: {}".format(controlsFileList[4]))
	print("6) Test6: {}".format(controlsFileList[5]))
	print("7) Test7: {}".format(controlsFileList[6]))
	print("8) Test8: {}".format(controlsFileList[7]))
	print("9) Test9: {}".format(controlsFileList[8]))
	print("")
	print("Press 'esc' to return")
	
	c = True
	while c == True:
		key = getch()

		if key == 49:
			c = False
			bind("Test1", 0)

		elif key == 50:
			c = False
			bind("Test2", 1)

		elif key == 51:
			c = False
			bind("Test3", 2)

		elif key == 52:
			c = False
			bind("Test4", 3)

		elif key == 53:
			c = False
			bind("Test5", 4)

		elif key == 54:
			c = False
			bind("Test6", 5)

		elif key == 55:
			c = False
			bind("Test7", 6)

		elif key == 56:
			c = False
			bind("Test8", 7)

		elif key == 57:
			c = False
			bind("Test9", 8)

		elif key == 27:
			c = False
			return False

def bind(action, index):
	clear()
	print("Press the key you want {} to be bound to:".format(action))
	newKey = getch()
	print(newKey)
	print("")
	print("Confirm: y or n")
			
	c = True
	while c == True:
		key = getch()
		if key == 121:
			c = False
			controlsFileList[index] = str(newKey) + "\n"

			with open('controls.txt', 'w') as controlsFile:
				controlsFile.truncate(0)
				controlsFile.writelines(controlsFileList)
			bindControls()

		elif key == 110:
			c = False
			bindControls()

def credits():
	clear()
	print("Designed and coded by an idiot named Nathan")
	print("'I'm not a bitch like you.'")
	print("")
	print("Copyright 2017 (lol but not actually...)")
	print("")
	print("Press 'esc' to return")
		
	c = True
	while c == True:
		key = getch()
		if key == 27:
			c = False
			mainMenu()

def quitMenu():
	clear()
	if saveStatus == False:
		print("You have not saved. Are you sure you want to quit to main menu?")
	else:
		print("Are you sure you want to quit to main menu?")
		print("")
		print("y or n")

	c = True
	while c == True:
		key = getch()
		if key == 121:
			c = False
			mainMenu()
		elif key == 110:
			c = False
			pauseMenu()

def quitGame():
	clear()
	if saveStatus == False:
		print("You have not saved. Are you sure you want to quit the game?")
	else:
		print("Are you sure you want to quit the game?")
	print("")
	print("y or n")

	c = True
	while c == True:
		key = getch()
		if key == 121:
			c = False
		elif key == 110:
			c = False
			return False
	
	clear()
	print("Goodbye!")
	time.sleep(1.5)
	clear()
	quit()

# Make Stuff Work Stuff
def main():
	startup()
	mainMenu()

if __name__ == "__main__":
	main()
