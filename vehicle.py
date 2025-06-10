Abstract method for vehicle 

from abc import ABC,abstractmethod

class vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
class car(vehicle):
    
    def start_engine(self):
        return "car engine started"
    
x = car()
print(x.start_engine())