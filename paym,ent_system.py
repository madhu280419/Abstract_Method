
from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
class creditcardpayment(payment):
    def pay(self,amount):
        return f"paid {payment} using AMEX card"
    
y = creditcardpayment()
print(y.pay(150))