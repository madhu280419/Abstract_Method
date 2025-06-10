from abc import ABC,abstractmethod

class account(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
    
    def deposit(self,amount):
        print(f"deposited {amount}")
        
class savingsaccount(account):
    def withdraw(self,amount):
        print(f"withdrawn {amount} from savings account")
        

class currentaccount(account):
    def withdraw(self,amount):
        print(f"withdrawn {amount} from current account")
        
s = savingsaccount()
s.deposit(500)
s.withdraw(250)

c = currentaccount()
c.deposit(2046)
c.withdraw(1027)
        