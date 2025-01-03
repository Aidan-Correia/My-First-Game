from re import X
import Attack
import Weapon
from enum import Enum

class Stats(Enum):
    SPEED = 0
    DEX = 1
    POWER = 2
    WISDOM = 3
    HP = 4
    
class Character:
    
    def __init__(self,name, stats, weapon, friendly = 0, items = None):
        self.name = name
        self.stats = stats
        self.weapon = weapon
        self.friendly = friendly
        self.currentHP = self.stats[Stats.HP.value()]
        if items == None:
            self.items = []
        self.x = -1
        self.y = -1
        
    def __str__(self):
        return self.name + " at " + "(" + self.x + "," + self.y + ")"
    

    def attack(self,target, attack):
        #calc scaling and damage
        #replace effect reference with switch statement based on effect type
        target.takeDamage(attack.damage, attack.damageType)
        
        effect = self.getNewEffect(attack.effectType)
        if attack.effect:
            attack.effect.applyEffect(self, target)
        pass
    

    def takeDamage(self, damage, damageType):
        #calc defenses based on damage type and take damage
        damageTaken = damage
        
        self.currentHP -= damageTaken
        if self.currentHP <= 0:
            self.currentHP = 0
        elif self.currentHP > self.stats[Stats.HP.value()]:
            self.currentHP = self.stats[Stats.HP.value()]
            
            
        
                


    def useItem(self, itemIndex):
        return self.items.pop(itemIndex)
        