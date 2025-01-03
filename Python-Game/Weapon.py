import Attack
from enum import Enum


class WeaponType(Enum):
    GAUNTLET = 0
    DAGGER = 1
    SWORD = 2
    GREATSWORD = 3
    AXE = 4
    GREATAXE = 5
    CLUB = 6
    GREATCLUB = 7
    STAFF = 8
    SPEAR = 9
    BOW = 10
    WAND = 11
    
class Stats(Enum):
    SPEED = 0
    DEX = 1
    POWER = 2
    WISDOM = 3
    HP = 4
    

   
class Weapon():
    
    def _init_(self, name, weaponType, statScaling, damageScaling, moveset = None):
        self.name = name
        self.weaponType = weaponType
        self.statScaling = statScaling
        self.damageScaling = damageScaling
        if moveset == None:
            moveset = []
            
    #adds moveid to moveset list, returns -1 if moveset is full        
    def addMove(self, move):
        if len(self.moveset) < 4:
            self.moveset.append(move)
        else:
            self.replaceMove(move)
            
    def replaceMove(self, move):
        print("Which move would you like to replace? \n")
        moveIndex = 0
        for move in self.moveset:
            print("enter " + moveIndex + " for " + move.name)
        
        invalid = True
        moveToReplace = 0
        while (invalid == True):
            try: 
               invalid = False
               moveToReplace = (int)(input("Make a Selection: "))
               assert ((moveToReplace >= 0) and (moveToReplace < 4))
            except:
                invalid = True
           
        self.moveset[moveToReplace] = move
            
  
       
        
        