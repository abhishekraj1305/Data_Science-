class Employee:
    def __init__(self):
        print("Employee class constructor called")
    a = 3
    
class Programmer(Employee):
    def __init__(self):
        print("Programmer class constructor called")
    b = 4
    
class manager(Programmer):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Programmer)
        print("Manager class constructor called")
    c = 5
    
m = manager()
print(m.a, m.b, m.c)

# d=Programmer()
# print(d.a, d.b)

# x = Employee()
# print(x.a)

