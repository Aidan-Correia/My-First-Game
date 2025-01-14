from enum import Enum

class DamageType(Enum):
		STATUS = -1
		STAB = 0
		SLASH = 1
		BLUDGEON = 2
		MAGIC = 3
		HEAL = 4
	

class Debuff(Enum):
	NOTHING = 0
	BLEED = 1
	POISON = 2
	ARMOR_BREAK = 3
	WEAKEN = 4
	PARALYZE = 5
	BLIND = 6
	



class Attack:

	def __init__(self, name, damage, damageType, range, effectType, effectChance):
		self.name = name
		self.damage = damage
		self.damageType = damageType
		self.range = range
		self.effectType = effectType
		self.effectChance = effectChance

	def __str__(self):
		returnString = self.name + ",\n"
		returnString += "DAMAGE: " + str(self.damage) + ",\n"
		returnString += "DAMAGE TYPE: " + str(self.damageType) + ",\n"
		returnString += "RANGE: " + str(self.range) + ",\n"
		returnString += "EFFECT: \n"
		if (self.effectType == 0):
			return returnString + "NONE"
		returnString += str(self.effectType)
		return returnString + "\nPROC CHANCE: " + str(self.effectChance)