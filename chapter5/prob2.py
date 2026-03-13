#wrp to input 8 numbers from user and display all unique no once

# numbers = set()  # Create an empty set to store unique numbers
# for i in range(8):
#     num = int(input("Enter a number: "))
#     numbers.add(num)  # Add the number to the set (duplicates will be ignored)  
# print("Unique numbers entered:", numbers)

s = set()  # Create an empty set to store unique numbers

n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)

print("Unique numbers entered:", s)