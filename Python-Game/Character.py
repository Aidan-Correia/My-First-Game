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
    
    def __init__(self, name, stats, weapon, friendly = 0, items = None):
        self.name = name
        self.stats = stats
        self.weapon = weapon
        self.friendly = friendly
        self.currentHP = self.stats[4]
        if items == None:
            self.items = []
        self.x = -1
        self.y = -1
        
    def __str__(self):
        alignment = "ENEMY"
        if (self.friendly == 1):
            alignment = "FRIENDLY"
        return "CHARACTER: " + self.name + ", \nSTATS: " + str(self.stats) + ", \n" + "TYPE: "+ alignment + "\nEQUIPPED WEAPON: \n\n" + str(self.weapon)
    
    def getNameAndPos(self):
        return self.name + " at " + "(" + self.x + "," + self.y + ")"

    def attack(self, target, attack):
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
        elif self.currentHP > self.stats[4]:
            self.currentHP = self.stats[4]
            
            
        
                
    def selectTarget(self, gameBoard):
        #crude target selection algorithm, first check what players can be reached this turn (within 3 squares), then, check what status conditions you can inflict based on your moveset
        #finally, check if you can inflict a status on any reachable players, if you can, move to that player (if necessary) and inflict him with a random status effect they are not yet afflicted by
        pass

    def useItem(self, itemIndex):
        return self.items.pop(itemIndex)
        