class Employee:
    company = "ITC Infotech"
    name = "John Doe"
    salary = 50000
    language = "Python"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} and the language is {self.language}")
        
        
class Coder:
    company = "ITC Infotech"
    language = "Python"
    def printLanguages(self):
        print(f"out of all the languages I know {self.language} is my favourite")
        
class programmer(Employee, Coder):
    # company = "ITC Infotech"
    def show_language(self):
        print(f"The name is {self.company} and he is Good at {self.language} language")
        
        
a = Employee()
b = programmer()
print(a.company, b.company)  # Accessing class attribute from Employee and programmer classes
b.show()  # Calling the show method from Employee class
b.printLanguages()  # Calling the printLanguages method from Coder class
b.show_language()  # Calling the show_language method from programmer class