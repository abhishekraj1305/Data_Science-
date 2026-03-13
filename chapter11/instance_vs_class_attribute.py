class Employee:
    language = "Python"  # Class attribute
    salary = 500000     # Class attribute
    name = "Abhishek"   # Class attribute
    
Abhishek = Employee()
print(Abhishek.name, Abhishek.salary, Abhishek.language) # Accessing class attributes through instance

Rohan = Employee()
Rohan.name = "Rohan"  # Creating instance attribute 'name' for Rohan
Rohan.salary = 60000  # Creating instance attribute 'salary' for Rohan
Rohan.language = "Java"  # Creating instance attribute 'language' for Rohan
print(Rohan.name, Rohan.salary, Rohan.language) # Accessing instance attributes for Rohan
print(Abhishek.name, Abhishek.salary, Abhishek.language) # Accessing class attributes for Abhishek, which remain unchanged
