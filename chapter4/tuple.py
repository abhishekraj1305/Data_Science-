a = (4,5,6,7,8,9,10,11,12,13,14,15)
print(type(a))  # <class 'tuple'>
print(a[0])  # Output: 4
print(a[-1]) # Output: 15
print(a[2:5])  # Output: (6, 7, 8
print(a[:3])   # Output: (4, 5, 6)
print(a[3:])   # Output: (7, 8, 9,

print(a[-4:])  # Output: (12, 13, 14, 15)
print(a[::2])  # Output: (4, 6, 8, 10, 12, 14)
print(a[1::3]) # Output: (5, 8, 11,
print(len(a))  # Output: 12
print(a.count(6))  # Output: 1


# a = tuple()
# type(a)  # <class 'tuple'>

# b = {}
# type(b)  # <class 'dict'>

# c = (3,)
# type(c)  # <class 'tuple'>


#Tuples are immutable, so we cannot change their elements
# a[0] = 10  # This will raise a TypeError: 'tuple' object does not support item assignment

#tupple methods
print(a.index(6))  # Output: 2
print(a.count(6))  # Output: 1
print(a)  # Output: (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print(a[0:5])  # Output: (4, 5, 6, 7, 8)
print(a.index(10))  # Output: 6
