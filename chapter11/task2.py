class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"
        
    def square(self):
        return self.num1 ** 2, self.num2 ** 2
    
    def cube(self):
        return self.num1 ** 3, self.num2 ** 3
    
    @staticmethod
    def Hello():
        print("Hello, welcome to the calculator!")
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

calc = calculator(num1, num2)
print(f"The sum of {num1} and {num2} is: {calc.add()}")
print(f"The difference of {num1} and {num2} is: {calc.subtract()}")
print(f"The product of {num1} and {num2} is: {calc.multiply()}")
print(f"The quotient of {num1} and {num2} is: {calc.divide()}")
square1, square2 = calc.square()
print(f"The square of {num1} is: {square1}")
print(f"The square of {num2} is: {square2}")
cube1, cube2 = calc.cube()
print(f"The cube of {num1} is: {cube1}")
print(f"The cube of {num2} is: {cube2}")

calculator.Hello()