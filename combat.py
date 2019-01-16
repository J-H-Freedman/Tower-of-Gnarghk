from dice import *

# There's got to be a way to import instances of objects in other files...
# Maybe create classes for each?
FOURdF = Dice(4, [-1, -1, 0, 0, 1, 1])
ONEd6 = Dice(1, [1, 2, 3, 4, 5, 6])

class Attack(object):
	def _MultiplyDamage(equipment, total_from_dice):
		'''Calculate total damage based on the player's weapon times a multiplier dictated by 4dF'''
		multiplier = math.sin(total_from_dice / 3) + 1
		if total_from_dice >= 4:
			return equipment * 3
			# you take a bonus turn
		elif total_from_dice <= -4:
			return 0
			# enemy takes a bonus turn
		else:
			return equipment * multiplier

	def _DistributeDamage(distribution_value, damage):
		'''Calculate where the damage goes based on the aim of 1d6'''
		damage_to_target = damage * ((distribution_value - 1) / 5) # find a way account for warped sides of the d6
		damage_to_body = damage - damage_to_target
		return int(damage_to_target), int(damage_to_body)
			#if distribution = 6:
			#	take another attack

	def Strike(equipment):
		'''calculate damage by using a multiplyer and then distribute it between the target and body'''
		roll_damage = FOURdF.RollAllDice()
		roll_aim = ONEd6.RollAllDice()
		damage_to_target, damage_to_body =  Attack._DistributeDamage(roll_aim, Attack._MultiplyDamage(equipment, roll_damage))
		return damage_to_target, damage_to_body

if __name__ == "__main__":
	def Main():
		sword = 100

		# to test damage multiplier
		for i in range(4, -5, -1): 
			print("damage is: ", Attack._MultiplyDamage(sword, i))

		# to test damage distribution
		for i in range(1, 7): 
			damage_to_target, damage_to_body = Attack._DistributeDamage(i, sword)
			print("damage to target is:", damage_to_target, "\n damage to body is:", damage_to_body)

		'''testing strike with printed explanation'''
		for i in range(10):
			damage_to_target, damage_to_body = Attack.Strike(sword)
			print(
				"damage to target is:", damage_to_target,
				"\n damage to body is:", damage_to_body
				)
		
		input("continue?")

	Main()