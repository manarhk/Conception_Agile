
import random
def singleton(cls):
       instance = [None]
       def wrapper(*args, **kwargs):
         if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
         return instance[0]
       return wrapper
@singleton
class Game:
    
    def __init__(self,name,mode,id=1) -> None:
        self.name=name
        self.mode=mode
        self.id = id 


    
    def id(self):
        return self.id
    