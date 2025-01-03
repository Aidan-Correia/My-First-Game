class Turn():
  
    def _init_(self, character, arena):
        self.character = character
        self.arena = arena
        


    def takeTurn(self):
        #if enemy, AI option select, else open select menu

    def menuSelect(self):
        #either end turn, move, or use attack (maybe add items in the future)
        pass
    

    def targetSelect(self, move):
        #select a target on the board given the move, only allow if target is within rang eof source, confirm proper target and execute character.attack(target, move)
        #check if target hp = 0, if so remove it from self.board and self.board.charlist
        pass

    def movementSelect(self):
        #characters can move speed/10 rounded down to an integer number of tiles per turn, can execute movement before or after an attack
        pass




