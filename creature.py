from dice import *
from combat import *

class Creature(object):
	def __init__(self, head, arm, legs):
		self.head = head
		self.arm = arm
		self.legs = legs

	'''
	the following is effectively pseudocode

	default head = 1
	default arm = 2
	default legs = 1 # 1 pair of legs to be targetted

	def dead(self):
		PlayDeathScreen() # needs to be made

	def offhandPenalty(self):
		remove self.d6.sides[6]

	def disarmed(self):
		def CoupDeGras():
			choose:
				Kill(enemy)
				Spare(enemy)
				Loot(enemy):
					then choose:
						Kill(enemy)
						Spare(enemy)

	def crippled(self):
		Enable_SkipFight()
		append self.d6.sides[1]

	while self.alive() == True:
		if head < 1:
			self.dead()
		if arm = 1:
			self.offhandPenalty()
		if arm < 1:
			self.disarmed()
		if legs < 1:
			self.crippled()

	each part can be assigned multiple attributes
	for example, a biting creature's head will be assigned "head" and "arm"

	'''