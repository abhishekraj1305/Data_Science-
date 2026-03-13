tup1 = (45,65,78,45,65,78,45,65,78,45,65,78)
tup2 = (45,65,78,45,65,78,45,65,78,45,65,78)

# tuple slicing
print(tup1[0])  # Output: 45
print(tup1[-1]) # Output: 78
print(tup1[2:5])  # Output: (78, 45, 65)
print(tup1[:3])   # Output: (45, 65, 78
print(tup1[3:])   # Output: (45, 65, 78, 45, 65, 78, 45, 65, 78)
print(tup1[-4:])  # Output: (45, 65, 78, 45)
print(tup1[::2])  # Output: (45, 78, 65, 78, 45, 78)
print(tup1[1::3]) # Output: (65, 45, 65, 45)
print(len(tup1))  # Output: 12  
print(tup1.count(45))  # Output: 4

tup3 = tup1 + tup2
print(tup3)  # Output: (45, 65, 78,

