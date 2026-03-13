class Number:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, num):
        return self.n + num.n
        
n = Number(5)
m = Number(10)

print(n + m)  # Output: 15, because we have overloaded the + operator to add the n attributes of the Number class instances n and m.

    
    