#arithmetic operator
a = 10
b = 5
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a % b)  # modulus
print(a ** b)  # exponentiation

#comparison operator
x = 10
y = 20
print(x == y)  # equal to
print(x != y)  # not equal to
print(x > y)   # greater than
print(x < y)   # less than
print(x >= y)  # greater than or equal to
print(x <= y)  # less than or equal to

#assignment operator
a = 10
a += 5  # equivalent to a = a + 5
print(a)  # 15
a -= 3  # equivalent to a = a - 3
print(a)  # 12
a *= 2  # equivalent to a = a * 2
print(a)  # 24
a /= 4  # equivalent to a = a / 4
print(a)  # 6.0
a %= 5  # equivalent to a = a % 5
print(a)  # 1.0

#logical operator
p = True
q = False
print(p and q)  # logical AND
print(p or q)   # logical OR
print(not p)    # logical NOT


#Truth Table for AND

print("Truth Table for AND",True and True)   # True
print("Truth Table for AND",True and False)  # False    
print("Truth Table for AND",False and True)  # False
print("Truth Table for AND",False and False) # False

#Truth Table for OR
print("Truth Table for OR",True or True)   # True
print("Truth Table for OR",True or False)  # True
print("Truth Table for OR",False or True)  # True
print("Truth Table for OR",False or False) # False

#Truth Table for NOT
print("Truth Table for NOT",not True)   # False
print("Truth Table for NOT",not False)  # True
