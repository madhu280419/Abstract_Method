from abc import ABC,abstractmethod
class device(ABC):
    @abstractmethod
    def power_on(self):
        pass
    
    def power_off(self):
        print("Device is shutting down")
        
class laptop(device):
    def power_on(self):
        print("power on")
        
class smartphone(device):
    def power_on(self):
        print("phone power on")
        
l = laptop()
l.power_on()
l.power_off()

s = smartphone()
s.power_on()
s.power_off()

