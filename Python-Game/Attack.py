from enum import Enum

class DamageType(Enum):
		STAB = 0
		SLASH = 1
		BLUDGEON = 2
		MAGIC = 3

class Debuff(Enum):
	NOTHING = 0
	BLEED = 1
	POISON = 2
	ARMOR_BREAK = 3
	WEAKEN = 4
	PARALYZE = 5
	BLIND = 6
	

class DamageType(Enum):
		STAB = 0
		SLASH = 1
		BLUDGEON = 2
		MAGIC = 3

class Attack:

	def _init_(self, name, damage, damageType, attackRange, effectType, effectChance):
		self.name = name
		self.damage = damage
		self.damageType = damageType
		self.range = attackRange
		self.effectType = effectType
		self.effectChance = effectChance