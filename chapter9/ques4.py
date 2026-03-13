#WRP of recurssive fxn to calculate sum on n natural numbers


"""sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + ... + n
sum(n) = n + sum(n - 1)"""


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


print(sum(10))

#Without using recursion, we can also calculate the sum of n natural numbers using the formula n*(n + 1) // 2
# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n*(n + 1) // 2
    
# print(sum(10))
