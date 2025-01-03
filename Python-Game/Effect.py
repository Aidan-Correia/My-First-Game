from abc import ABC, abstractclassmethod


class Effect(ABC):
    
    @abstractclassmethod
    def _init_(self):
       pass
   
    @abstractclassmethod
    def applyEffect(self, source, target):
        pass