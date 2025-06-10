from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def eat(self):
        print("dog is eating")
    def sound(self):
         print("BOW BOW")
obj = Dog()
print(obj.eat())