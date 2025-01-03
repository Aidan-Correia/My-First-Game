class Arena():
    

    def _init_(self, party, encounter):
        self.grid = [[0 for _ in range(5)] for _ in range(5)]
        self.turn = 0
        self.turnOrder = []
        self.getTurnOrder(self, party, encounter.enemyList)
       
        #party[0] goes to 2,1  party[1] goes to 1,0,   party[2] goes to 2,0  and opposite for enemies
        #then all characters are added to the characterlist which is sorted by speed (used for priority, even if speed changes (due to paralsis etc) this order remians constant through the whole battle)
        

    #given array of party members and array of enemy party members, order them by speed decreasing, and set the turn order equal to that
    def getTurnOrder(self, party, enemies):
        
        while ((len(party) > 0) and (len(enemies) > 0)):
            maxSpeed = party[0]
            maxIndex = 0
            currentIndex = 0
            partyOrEnemy = 0
            while (currentIndex < max(len(party), len(enemies))):
                if currentIndex < len(party):
                    if party[currentIndex].stats[0] > maxSpeed:
                        maxSpeed = party[currentIndex].stats[0]
                        maxIndex = currentIndex
                        partyOrEnemy = 0
                if currentIndex < len(enemies):
                    if enemies[currentIndex].stats[0] > maxSpeed:
                        maxSpeed = enemies[currentIndex].stats[0]
                        maxIndex = currentIndex
                        partyOrEnemy = 1


                currentIndex += 1
            if partyOrEnemy == 0:
                self.turnOrder.append(party.pop(maxIndex))
            else:
                self.turnOrder.append(enemies.pop(maxIndex))
                
                
    def checkBattleOver(self):
        if len(self.turnOrder <  1):
            return True
        siding = self.turnOrder[0].friendly
        for c in self.turnOrder:
            if c.friendly != siding:
                return -1
        return siding

    def killCharacter(self, character):
        self.turnOrder.remove(character)
        self.grid[character.x][character.y] = 0
        print(str(character) + " has been slain")
        battleResult = self.checkBattleOver
        if battleResult != 0:
            return
            #end battle if winner, move onto next battle, else game over screen
        return
        
        
            

