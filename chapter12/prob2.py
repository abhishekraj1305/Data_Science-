class Animals:
    pass

class pets(Animals):
    pass

class dog(pets):
    
    @staticmethod
    def bark():
        print("Woof! Woof!")
d = dog()
d.bark()