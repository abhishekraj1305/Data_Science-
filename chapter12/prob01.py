class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f"TwoDVector: x={self.x}, y={self.y}")   
        
class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Call the constructor of the parent class (TwoDVector) to initialize x and y
        self.z = z  # Initialize z in the ThreeDVector class


    def show(self):
        super().show()  # Call the show method of the parent class (TwoDVector) to display x and y
        print(f"ThreeDVector: z={self.z}")  # Display z in the ThreeDVector class

        
v = ThreeDVector(1, 2, 3)
print(v.x, v.y, v.z)  # Output: 1 2 3, because we have called the constructor of the parent class (TwoDVector) to initialize x and y, and we have initialized z in the ThreeDVector class.
v.show()  # Output: TwoDVector: x=1, y=2 and ThreeDVector: z=3, because we have called the show method of the parent class (TwoDVector) to display x and y, and we have displayed z in the ThreeDVector class.

a = TwoDVector(4, 5)
print(a.x, a.y)  # Output: 4 5, because we have
a.show()  # Output: TwoDVector: x=4, y=5, because we have called the show method of the TwoDVector class to display x and y.