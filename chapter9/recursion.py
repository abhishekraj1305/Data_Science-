"""factorial of n is n * factorial of (n-1)
factorial of 0 is 1
factorial of 1 is 1
factorial of 5 is 5 * factorial of 4
factorial of 4 is 4 * factorial of 3
factorial of 3 is 3 * factorial of 2
factorial of 2 is 2 * factorial of 1
factorial of 1 is 1
factorial of 5 is 5 * 4 * 3 * 2 * 1
factorial of 5 is 120
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")