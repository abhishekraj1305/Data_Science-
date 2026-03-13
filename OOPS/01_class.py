#class are the blueprint of an oblect 

class Employee:
    company = "HP"
    
    def get_salary(self):
        return 35000
    
e = Employee()
print(e.get_salary())