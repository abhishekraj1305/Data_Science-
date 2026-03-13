class Employee:
    company = "ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} and the language is {self.language}")
        
class programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} and the language is {self.language}")
        
    def show_language(self):
        print(f"The name is {self.name} and he is Good at {self.language} language")
        
a = Employee()
b = programmer()

print(a.company, b.company)  # Accessing class attribute from Employee and programmer classes