class Programmers:
    company = "Microsoft"  # Class attribute
    
    def __init__(self, name, salary, language):
        self.name = name  # Instance attribute
        self.salary = salary  # Instance attribute
        self.language = language  # Instance attribute
        
Abhishek = Programmers("Abhishek", 50000, "Python")
print(Abhishek.name, Abhishek.salary, Abhishek.language, Programmers.company)

Vinit = Programmers("Vinit", 60000, "Java")
print(Vinit.name, Vinit.salary, Vinit.language, Programmers.company)

Rohan = Programmers("Rohan", 70000, "C++")
print(Rohan.name, Rohan.salary, Rohan.language, Programmers.company)