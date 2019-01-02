import random
import math

class Dice(object):
	def __init__(self, number, sides, probability):
		self._number = number
		self._sides = sides
		self._probability = probability

	def RollDie(self):
		return random.choice(self._sides)

	def RollAllDice(self):
		total_from_dice = 0

		for i in range(self._number):			
			total_from_dice += self.RollDie()

		return total_from_dice

class Fudge(Dice):
	def __init__(self):
		self._number = 4
		self._sides = [-1, -1, 0, 0, 1, 1]
		self.__probability__ = {
			4 : 1/81,
			3 : 4/81,
			2 : 10/81,
			1 : 16/81,
			0 : 19/81,
			-1 : 16/81,
			-2 : 10/81,
			-3 : 4/81,
			-4 : 1/81
		}

	def Multiplier(self, equipment, total_from_dice):
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
		self._number = 1
		self._sides = [1, 2, 3, 4, 5, 6]
		self.__probability__ = {
			1 : (1/6), 
			2 : (1/6), 
			3 : (1/6), 
			4 : (1/6), 
			5 : (1/6), 
			6 : (1/6)
		} # there's got to ge a better way using range or a for loop or something

	def Distribution(self, distribution, damage):
		damage_to_target = damage * (distribution / 6)
		damage_to_body = damage - (damage_to_target)
		return damage_to_target, damage_to_body
			#if distribution = 6:
			#	take another attack

def Attack(equipment, fudge_dice, d6_die):
	return d6.Distribution(d6_die, Fudge.Multiplier(equipment, fudge_dice))

if __name__ == "__main__":
	def Main():
		Fudge_dice = Fudge()
		d6_die = d6()
		sword = 10

		#print(d6_die.RollDie())
		#print(Fudge_dice.RollDie())
		#print(d6_die.RollAllDice())
		#print(Fudge_dice.RollAllDice())

		# to test damage multiplier
		for i in range(4, -5, -1): 
			print("damage is: ", Fudge_dice.Multiplier(sword, i))

		# to test damage distribution
		for i in range(1, 7): 
			damage_to_target, damage_to_body = d6_die.Distribution(i, sword)
			print("damage to target is:", damage_to_target, "\n damage to body is:", damage_to_body)

		print(Attack(sword, Fudge_dice.RollAllDice(), d6_die.RollAllDice()))


	Main()