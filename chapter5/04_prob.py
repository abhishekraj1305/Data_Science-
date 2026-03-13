s = set()

s.add(1)
s.add(1.0)  # This will not be added to the set because 1 and 1.0 are considered equal in Python
s.add('1')  # This will be added to the set because '1' is a string and is different from the integer 1
print(len(s))  # Output: {1, '1'}