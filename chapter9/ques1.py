

a = 1
b = 2
c = 3

def greatest(a,b,c):
    if a > b and a > c:
        print(f"{a} is greatest")
        return a
    elif b > a and b > c:
        print(f"{b} is greatest")
        return b
    else:
        print(f"{c} is greatest")
        return c
        
a = 10000
b = 98
c = 40

print(greatest(a,b,c))