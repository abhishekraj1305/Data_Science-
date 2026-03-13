class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"class attribute of a is {cls.a}")
        
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
        
e = Employee()
e.a = 45
e.show()  # Output: class attribute of a is 45, because show is a class method and it accesses the class attribute a, not the instance attribute a.

e.name = "Abhishek Raj"
print(e.name)  # Output: Abhishek, because we have set the name property to "Abhishek" using the setter method, and we are accessing it using the getter method.