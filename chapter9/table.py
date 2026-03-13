#WRP To Print multiple table of Given Number


    
# def multiplication_table():
#     num = int(input("Enter a number: "))
#     print(f"Multiplication table of {num} using for loop:")
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")

# def multiplication_table(num):
#     print(f"\nTable of {num}:")
#     for i in range(1, 11):
#         # result = num * i
#         print(f"{num} x {i} = {num * i}")
#         # return f"{num} x {i} = {num * i}"
        
        
# multiplication_table(5)        
# print(multiplication_table(10))


def multiply(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        
n = int(input("Enter a number: "))
multiply(n)