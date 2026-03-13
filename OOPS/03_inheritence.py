class Animal:
    location = "India"
    def __init__(self,name):
        self.name =name
        
        
    def speak(self):
        print("Generic animal Sound")
        
        
class Dog(Animal):
    def speak(self):
        print("Woof!!!")



d = Dog("Sheru")
print(d.name)
d.speak()
print(d.location)
    