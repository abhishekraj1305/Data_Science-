#constrctor is a special method in python which is used to initialize the object of a class. It is called when an object of the class is created. The constructor is defined using the __init__ method.

class Employee:
    
    name = "Abhishek"  # Class attribute
    language = "Python"  # Class attribute
    salary = 500000     # Class attribute
    
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        
    def getinfo(self):
        print(f"Name is : {self.name}, Salary is: {self.salary}, Language is: {self.language}")
        
    @staticmethod
    def company_policy():
        print("Company policy: All employees must adhere to the code of conduct and maintain professionalism at all times.")
        
        
Abhishek = Employee("Aashu", 1000000, "Python")
Raushan = Employee("Raushan", 600000, "Java")
Abhishek.getinfo()
Raushan.getinfo()
Employee.company_policy()  # Calling the static method using the class name