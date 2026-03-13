#WRP To Find Factorial


n = int(input("Enter a number: "))



# def factorial_func(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         factorial = 1
#         for i in range(2, n + 1):            
#             factorial *= i
#         return factorial
    
# print(f"Factorial of {n} is: {factorial_func(n)}")

product = 1
for i in range(1, n + 1):
    if i == 1:
        factorial = 1
    else:
        product *= i
        # factorial = product
print(f"Factorial of {n} is: {product}")