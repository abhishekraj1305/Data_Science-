class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of Employee is {self.name} and the salary is {self.salary}, the bond of the employee is {self.bond} years")
        
        
a1 = Employee(50000, "Abhishek", 4)
a1.get_info()