s1 = {1,45,76,45,65,78,45,65,78,45,65,78}
s2 = {45,65,78,45,65,78,45,65,78,45,65,78}




print({45,65,78}.issubset(s1))  # Output: True
print({45,65,78}.issuperset(s1))  # Output: False





# print(s1.union(s2))  # Output: {1, 45, 65, 76, 78}
# print(s1.intersection(s2))  # Output: {45, 65, 78}
# print(s1.difference(s2))  # Output: {1}
# print(s1.symmetric_difference(s2))  # Output: {1}

# print(s1 | s2)  # Output: {1, 45, 65, 76, 78}
# print(s1 & s2)  # Output: {45, 65, 78
# print(s1 - s2)  # Output: {1}
# print(s1 ^ s2)  # Output: {1}
# print(s1.issubset(s2))  # Output: False
# print(s1.issuperset(s2))  # Output: False
# print(s1.isdisjoint(s2))  # Output: False
# print(len(s1))  # Output: 4
# print(45 in s1)  # Output: True
# print(s1.copy())  # Output: {1, 45, 65, 76, 78}
# # s1.clear()
# # print(s1)  # Output: set()

