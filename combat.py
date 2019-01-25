from dice import *

# Lots of dead variables.  Create an equipment file.

class Damage:
	def _RollDamage(self, weapon_dice):
		return weapon_dice.Roll()

	def Multiplier(self, damage_result, multiplier_result):
		'''Calculate total damage based on the player's weapon times a multiplier dictated by 4dF'''
		multiplier = math.sin(multiplier_result / 3) + 1
		if multiplier_result >= 4:
			return damage_result * 3
			# you take a bonus turn
		elif multiplier_result <= -4:
			return 0
			# enemy takes a bonus turn
		else:
			return damage_result * multiplier

	def Distribute(self, distribution_result, multiplied_damage):
		'''Calculate where the damage goes based on the aim of 1d6'''
		damage_to_target = multiplied_damage * ((distribution_result - 1) / 5) # find a way account for warped sides of the d6
		excess_damage = multiplied_damage - damage_to_target
		return int(damage_to_target), int(excess_damage)
			#if distribution = 6:
			#	take another attack

class SuccessfulAttack:
	def _CalcualteBlocked(self, damage_result):
		'''calculate damage by using a multiplyer and then distribute it between the target and body'''
		damage_to_arm, damage_to_shield = Damage.Distribute(roll_aim, self._CalculateStandard(damage_result))
		return damage_to_arm, damage_to_shield

	def _CalculateStandard(self, damage_result):
		return Damage.Multiplier(damage_result, roll_damage)

class AimWeapon:
	def _Calculate(self, aim_threshold, aim_result):
		if aim_result > aim_threshold:
			return aim == True
		elif aim_result == aim_threshold:
			return glancing_blow == True
		else:
			return aim == False

	def GetAccuracy(self, equipment):
		return self._Calculate(equipment.HitChance, AccuracyDie.Roll())

'''
if __name__ == "__main__":
	sword = Dice(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	FOURdF = Dice(4, [-1, -1, 0, 0, 1, 1])
	ONEd6 = Dice(1, [1, 2, 3, 4, 5, 6])

	# to test damage multiplier
	for i in range(4, -5, -1): 
		print("damage is: ", Damage._Multiplier(sword, i))

	# to test damage distribution
	for i in range(1, 7): 
		damage_to_target, damage_to_body = Damage.Distribute(i, sword)
		print("damage to target is:", damage_to_target, "\n damage to body is:", damage_to_body)

	#testing strike with printed explanation
	for i in range(10):
		damage_to_target, damage_to_body = Damage.Strike(sword)
		print(
			"damage to target is:", damage_to_target,
			"\n damage to body is:", damage_to_body
			)
	
	input("continue?")

	'''