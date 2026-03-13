class Employee:
    a = 3
    
class Programmer(Employee):
    b = 4
    
class manager(Programmer):
    c = 5
    
m = manager()
print(m.a, m.b, m.c)

d=Programmer()
print(d.a, d.b)

x = Employee()
print(x.a)

