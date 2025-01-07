from venv import create
from Attack import Attack
from Weapon import Weapon
from Character import Character
import json
import os
from enum import Enum

class DamageType(Enum):
    STATUS = 0   
    STAB = 1
    SLASH = 2
    BLUDGEON = 3
    MAGIC = 4

class Debuff(Enum):
    NOTHING = 0
    BLEED = 1
    POISON = 2
    WEAKEN = 3
    PARALYZE = 4
    BLIND = 5
    
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

def createAttack(dict):
    attack = Attack(dict["name"], dict["damage"], dict["damageType"], dict["range"], dict["debuff"], dict["debuffChance"])
    return attack

def createWeapon(dict):
    weapon = Weapon(dict["name"], dict["weaponType"], dict["statScaling"], dict["damageScaling"])
    for atk in dict["startingMoves"]:
        weapon.addMove(createAttack(atk))

    return weapon

def createChar(dict):
    weaponAsDict = dict["startingWeapon"]
    weapon = createWeapon(weaponAsDict)
    character = Character(dict["name"], dict["stats"], weapon, 1)
    return character
   

def selectCharacter(characters, charType):
    characterIndices = 0
    arrCharID = []
    print("Party " + charType + " select \n \n")
    for character in characters:
        characterIndices = characterIndices + 1 
        arrCharID.append(character["characterID"])
        
        print(f"{characterIndices}: \n \t {character['name']} \n \t Speed: {character['stats'][0]} \n \t Dex: {character['stats'][1]} \n \t Power: {character['stats'][2]} \n \t Wisdom: {character['stats'][3]} \n \t HP: {character['stats'][4]}")
        print(f"\n \t Character Description: {character['description']}")        

    print("\n \n")
    invalidInput = True
    while (invalidInput):
        characterSelect = input("Enter a value (1-" + str(characterIndices) + ") to select a party " + charType + " \n")
        try:
            characterSelect = (int)(characterSelect)
            assert(characterSelect in range(characterIndices+1))
            invalidInput = False
        except:
            print("Invalid Input")
            invalidInput = True

    charChoiceDict = characters[characterSelect-1]
    charChoice = createChar(charChoiceDict)

    del characters[characterSelect-1]
    
    return charChoice
    


def selectParty():
    partyList = []    

    path = "data\characters.json"
    charFile = open(path, "r")
    charsAsJSON = charFile.read()
    characters = json.loads(charsAsJSON)
    
    partyList.append(selectCharacter(characters["leaders"], "leader"))
    #create char object
    
    partyList.append(selectCharacter(characters["followers"], "member"))
    #create char object
    
    
    partyList.append(selectCharacter(characters["followers"], "member"))
    #create char object
    return partyList


def mainMenuSelect():
    menuSelect = input("Welcome to my game! \n enter 1 to start a run \n enter 0 to exit \n")
    inputValid = False
    if (menuSelect == "1" or menuSelect == "0"):
        inputValid = True
    while(inputValid == False):
        menuSelect = input("Please enter a valid selection\n")
        if (menuSelect == "1" or menuSelect == "0"):
            inputValid = True
            
    return menuSelect

def runGameLoop():
    gameRunning =  (int)(mainMenuSelect())
    while gameRunning:
        partyList = selectParty()
        for member in partyList:
            print(member)
        gameRunning = False
       
    print("Come back soon!")
    return
            
def main():
    runGameLoop()
    


if __name__ == "__main__":
    main()