import random
import math

class Dice(object):
	def __init__(self, number, sides, probability):
		self.number = number
		self.sides = sides
#		self.probability = probability

	def RollDie(self):
		return random.choice(self._sides)

	def RollAllDice(self):
		''' Standard dice roll'''
		total_from_dice = 0

		for i in range(self._number):			
			total_from_dice += self.RollDie()

		return total_from_dice

class Fudge(Dice):
	def __init__(self):
		self.number = 4
		self.sides = [-1, -1, 0, 0, 1, 1]
#		self.__probability__ = {
#			4 : 1/81,
#			3 : 4/81,
#			2 : 10/81,
#			1 : 16/81,
#			0 : 19/81,
#			-1 : 16/81,
#			-2 : 10/81,
#			-3 : 4/81,
#			-4 : 1/81
#		}

	def Multiplier(self, equipment, total_from_dice):
		'''Calculate total damage based on the player's weapon times a multiplier dictated by 4dF'''
		multiplier = math.sin(total_from_dice / 3) + 1
		if total_from_dice == 4:
			return equipment * 3
			# you take a bonus turn
		elif total_from_dice == -4:
			return 0
			# enemy takes a bonus turn
		else:
			return equipment * multiplier

class d6(Dice):
	def __init__(self):
		self.number = 1
		self.sides = [1, 2, 3, 4, 5, 6]
#		self.__probability__ = {
#			1 : (1/6), 
#			2 : (1/6), 
#			3 : (1/6), 
#			4 : (1/6), 
#			5 : (1/6), 
#			6 : (1/6)
#		}

	def Distribution(self, distribution_value, damage):
		'''Calculate where the damage goes based on the aim of 1d6'''
		damage_to_target = damage * ((distribution_value - 1) / 5)
		damage_to_body = damage - damage_to_target
		return int(damage_to_target), int(damage_to_body)
			#if distribution = 6:
			#	take another attack

if __name__ == "__main__":
	def Main():
		sword = 100

		# to test damage multiplier
		for i in range(4, -5, -1): 
			print("damage is: ", Fudge().Multiplier(sword, i))

		# to test damage distribution
		for i in range(1, 7): 
			damage_to_target, damage_to_body = d6().Distribution(i, sword)
			print("damage to target is:", damage_to_target, "\n damage to body is:", damage_to_body)

	Main()