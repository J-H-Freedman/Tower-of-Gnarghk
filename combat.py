from dice import *

def Strike(equipment):
	'''calculate damage by using a multiplyer
	and then distribute it between the target and body'''
	roll_damage = Fudge().RollAllDice()
	roll_aim = d6().RollAllDice()
#	TEST = 100
#	if equipment == TEST:
#		for i in range(4, -5, -1):
#			roll_damage = i
#			for i in range(1, 7):
#				roll_aim = i
#				print(d6().Distribution(roll_aim, Fudge().Multiplier(equipment, roll_damage)))
	target_damage_from_strike, body_damage_from_strike = d6().Distribution(
		roll_aim, Fudge().Multiplier(equipment, roll_damage)
		)
	return target_damage_from_strike, body_damage_from_strike

if __name__ == "__main__":
	def Main():
		sword = 100

		'''testing strike with printed explanation'''
		target_damage_from_strike, body_damage_from_strike = Strike(sword)
		print(
			"damage to target is:", target_damage_from_strike,
			"\n damage to body is:", body_damage_from_strike
			)

#		TEST = 100
#		Strike(TEST)		
		input("continue?")

	Main()