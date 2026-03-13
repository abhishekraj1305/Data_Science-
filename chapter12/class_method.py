class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"class attribute of a is {cls.a}")
        
        
e = Employee()
e.a = 45
e.show()  # Output: class attribute of a is 45, because show is a class method and it accesses the class attribute a, not the instance attribute a.