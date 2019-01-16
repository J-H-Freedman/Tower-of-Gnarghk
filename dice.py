import random
import math

# Create Dice
class Dice(object):
	def __init__(self, number, sides):
		self._number = number
		self._sides = sides

	def _RollDie(self):
		return random.choice(self._sides)

	def RollAllDice(self):
		''' Standard dice roll'''
		total_from_dice = 0

		for i in range(self._number):			
			total_from_dice += self._RollDie()

		return total_from_dice

# Commonly Used dice
FOURdF = Dice(4, [-1, -1, 0, 0, 1, 1])
ONEd6 = Dice(1, [1, 2, 3, 4, 5, 6])

# Testing...
if __name__ == "__main__":
	def Main():
		sword = 100

		# to test dice
		for i in range(10):
			print("The F roll is", FOURdF.RollAllDice())
			print("The d6 roll is", ONEd6.RollAllDice())

	Main()