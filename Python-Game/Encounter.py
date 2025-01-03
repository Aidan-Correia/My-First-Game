class Encounter():
    
    def _init_(self, difficulty, enemyList = None):
        self.difficulty = difficulty 
        if enemyList == None:
            enemyList = []
        

    def addEnemy(self, enemy):
        if len(self.enemyList) < 3:
            self.enemyList.append
        else:
            return -1



