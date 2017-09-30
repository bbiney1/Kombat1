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

# Player
class player:
	name = "Shitlord"
	hp = 150
	hpMax = 150
	stamina = 1

# Enemies
class simpleEnemy:
	name = "Goblin"
	hp = 100
	hpMax = 100
	moveSet = [["A", "N"], ["N", "D"], ["D", "N"], ["N", "A"]]
	
def combat(enemy):
	roundNumber = 1
	while player.hp != 0 or enemy.hp != 0:
		moveNumber = 0
		roundOver = False
		playerStamina = player.stamina
		move = [" "]
		for x in range(playerStamina):
			move.append(" ")

		while playerStamina != 0:
			clear()
			print("Round {}".format(roundNumber))
			print("A = Attack, D = Defense, S = Special Attack, F = Special Defense, M = Use Magic, I = Use Item, N = No Action")
			print("")
			print(player.name)
			print("HP: {}/{}".format(player.hp, player.hpMax))
			print("Stamina: {}".format(playerStamina))
			print("")
			print("| {} | {} |".format(move[0], move[1]))
			print("")
			print("")
			print(enemy.name)
			print("HP: {}/{}".format(enemy.hp, enemy.hpMax))
			print("")
			print("|   |   |")

			c = True
			while c == True:
				key = getch()
				
				if key == 97:
					c = False
					move[(moveNumber)] = "A"
					playerStamina = playerStamina - 1
					moveNumber = moveNumber + 1

				elif key == 100:
					c = False
					move[(moveNumber)] = "D"
					playerStamina = playerStamina - 1
					moveNumber = moveNumber + 1

				elif key == 115:
					c = False
					move[(moveNumber)] = "S"
					playerStamina = playerStamina - 2
					moveNumber = moveNumber + 1

				elif key == 102:
					c = False
					move[(moveNumber)] = "F"
					playerStamina = playerStamina - 2
					moveNumber = moveNumber + 1

				elif key == 109:
					c = False
					move[(moveNumber)] = "M"
					playerStamina = playerStamina - 3
					moveNumber = moveNumber + 1

				elif key == 105:
					c = False
					move[(moveNumber)] = "I"
					playerStamina = playerStamina - 1
					moveNumber = moveNumber + 1

				elif key == 110:
					c = False
					move[(moveNumber)] = " "
					moveNumber = moveNumber + 1

			if moveNumber == 2:
				roundOver = True

		roundNumber = roundNumber + 1
		
		if roundNumber == 5:
			quit()


def main():
	clear()
	print("Begin test? y or n")

	c = True
	while c == True:
		key = getch()

		if key == 121:
			c = False
			combat(simpleEnemy())

		elif key == 110:
			c = False
			quit()

if __name__ == "__main__":
    main()
