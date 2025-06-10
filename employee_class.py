from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
       pass
    
    def show_details(self):
        print("Employee details displayed.")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return "Full-time salary calculated."

class Freelancer(Employee):
    def calculate_salary(self):
        return "Freelancer salary calculated."

emp1 = FullTimeEmployee()
print(emp1.calculate_salary())
emp1.show_details()

emp2 = Freelancer()
print(emp2.calculate_salary())
emp2.show_details()