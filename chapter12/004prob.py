class Employee:
    salary = 10000
    increment = 20
    
    
    @property
    def salary_after_increment(self):
        return self.salary + (self.salary * self.increment / 100)
    
    @salary_after_increment.setter
    def salary_after_increment(self, value):
        self.increment = (value - self.salary) / self.salary * 100 if self.salary != 0 else 0
        
    
e = Employee()
print(e.salary_after_increment)  # Output: 12000.0, because the salary is 10000 and the increment is 20%, so the salary after increment is 10000 + (10000 * 20 / 100) = 12000.0

e.salary_after_increment = 15000
print(e.increment)  # Output: 50.0, because we have set the salary after increment to 15000, so the increment is (15000 - 10000) / 10000 * 100 = 50.0