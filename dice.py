import random
import math

# Create Dice
class Die:
	def __init__(self, die_sides):
		self.die_sides = die_sides

	@staticmethod
	def Generator(number_of_sides):
		'''Generate die based on the number of sides'''
		return [i for i in range(1, number_of_sides + 1)]

	def Roll(self):
		'''Get random side from die'''
		return random.choice(die_sides)

	def GetDie(self):
		return self.die_sides

	def AddSide(self, side):
		self.die_sides.append(side)

	def RemoveSide(self, side):
		self.die_sides.remove(side)

class Dice:
	def __init__(self, number_of_dice, die_type):
		self._number_of_dice = number_of_dice
		self._die_type = die_type

	@staticmethod
	def Generator(self, number_of_dice, number_of_sides):
		'''Generate dice based on the number of sides'''
		return number_of_dice, Die.Generator(number_of_sides)

	def Roll(self):
		'''Add random sides from dice'''
		GetDie(die_type)

		total_from_dice = 0

		for i in range(self._number_of_dice):			
			total_from_dice += die_type.Roll()

		return total_from_dice

	def GetAllDice(self):
		return self._number_of_dice, self._die_type

	def ChangeDiceAmount(self, new_amount):
		return self._number_of_dice = new_amount

	def ChangeDiceType(self, new_type):
		return self._die_type = new_type

'''
# Testing...
# fix main
if __name__ == "__main__":
	sword = 100

	# Commonly Used dice
	dF = Die([-1, -1, 0, 0, 1, 1])
	d6 = Die([1, 2, 3, 4, 5, 6])
	FOURdF = Dice(4, dF)
	ONEd6 = Dice(1, d6)

	# to test dice
	for i in range(10):
		print("The F roll is", FOURdF.Roll())
		print("The d6 roll is", ONEd6.Roll())
		'''