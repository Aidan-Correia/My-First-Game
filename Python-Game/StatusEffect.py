from Effect import Effect
from abc import ABC, abstractclassmethod

class StatusEffect(Effect):
    name = 'Nothing'
    baseDuration = 10
    
    @abstractclassmethod
    def _init_(self):
        pass
   
   
    @abstractclassmethod
    def applyEffect(self, source, target):
        if self not in target.debuffs:    
            target.debuffs.add(self)
            print(f"{str(target)} afflicted with {self.name}")
        
    
    #called every turn, (poison/bleed apply damage, )
    @abstractclassmethod
    def updateStatus(self, target):
        pass
    
    
    def removeStatus(self, target):
        target.debuffs.remove(self)


class PoisonEffect(StatusEffect):
    name = 'Poison'    
    damage = 2
    

    def _init_(self, durationModifier = 1):
        self.duration = self.baseDuration*durationModifier

    
    def applyEffect(self, source, target):
        super().applyEffect
        
    
   
    def updateStatus(self, target):
        target.takeDamage(self.damage, -1)
        self.duration -= 1
        if self.duration <= 0:
            self.removeStatus(target)

    

class BleedEffect(StatusEffect):
    name = 'Bleed'    
    damage = 2
    

    def _init_(self, durationModifier = 1):
        self.duration = self.baseDuration*durationModifier

    
    def applyEffect(self, source, target):
        super().applyEffect
        
    
   
    def updateStatus(self, target):
        target.takeDamage(self.damage, -1)
        self.duration -= 1
        if self.duration <= 0:
            self.removeStatus(target)
    
