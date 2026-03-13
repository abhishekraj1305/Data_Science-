#WRP to print multiplication table of n using for loop in Reverse order


n = int(input("Enter a number: "))

#Method 1 (Reverse Range)	
# for i in range(10, 0, -1):
#     print(f"{n} x {i} = {n * i}")
    
#Method 2 (Reversed Range)
# for i in range(1, 11):
#     print(f"{n} x {11-i} = {n * (11-i)}")
    
#Method 3 (Reversed Function) Best Method
for i in reversed(range(1, 11)):
    print(f"{n} x {i} = {n * i}")