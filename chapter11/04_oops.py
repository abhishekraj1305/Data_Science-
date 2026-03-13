class Employee:
    name = "Abhishek"
    salary = 50000
    language = "Python"
    
    def getinfo(self):
        print(f"Name is : {self.name}, Salary is: {self.salary}, Language is: {self.language}")
        
    def greet(self):
        print(f"Hello {self.name}, welcome to the company!")
        
    @staticmethod
    def company_policy():
        print("Company policy: All employees must adhere to the code of conduct and maintain professionalism at all times.")
        
Abhishek = Employee()
Abhishek.getinfo()
Abhishek.greet()
Employee.company_policy()  # Calling the static method using the class name
# Abhishek.language = "Java"  # Modifying the class attribute 'language' for the instance Abhishek
# print(Abhishek.name,Abhishek.salary,Abhishek.language)
# Abhishek.getinfo()
# vinit = Employee()
# vinit.name = "Vinit"
# vinit.salary = 60000
# vinit.language = "C++"
# Employee.getinfo(vinit)  # Calling the method using the class name and passing the instance as an argument