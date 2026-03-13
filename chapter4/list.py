#list tutorial
import copy
friends = ["Abhishek", "Rahul", "Rohit", "Satyarth", "Shivam", "Anshul", "Satyarth", "Shivam", "Anshul", "Satyarth", "Shivam", "Anshul", "Satyarth", "Shivam", "Anshul"]
print(friends[4])  # Output: "Shivam"
print(friends[-1]) # Output: "Anshul"
print(friends[2:5])  # Output: ["Rohit", "Satyarth", "Shivam"]
print(friends[:3])   # Output: ["Abhishek", "Rahul", "Rohit"]
print(friends[3:])   # Output: ["Satyarth", "Shivam", "Anshul", "Satyarth", "Shivam", "Anshul", "Satyarth", "Shivam", "Anshul", "Satyarth", "Shivam", "Anshul"]
print(friends[-4:])  # Output: ["Satyarth", "Shivam", "Anshul", "Satyarth", "Shivam", "Anshul"]
print(friends[::2])  # Output: ["Abhishek", "Rohit", "Shivam", "Satyarth", "Anshul", "Satyarth", "Anshul"]
print(friends[1::3]) # Output: ["Rahul", "Satyarth", "Anshul", "Shivam", "Satyarth"]    


# string slicing
friends[0] = "Abhi"
print(friends)  # Output: ["Abhi", "Rahul", "Rohit", "Satyarth", "Shivam", "Anshul", "Satyarth", "Shivam", "Anshul", "Satyarth", "Shivam", "Anshul", "Satyarth", "Shivam", "Anshul"]

print(len(friends))  # Output: 14
print(friends.count("Satyarth"))  # Output: 4


# print(friends[4[2]]) #Wrong Syntax
print(friends[4][2])

#list methods
friends.append("Satapal")
friends.insert(2, "Satya")
friends.remove("Rohit")
friends.pop()  # removes the last element
friends.sort()  # sorts the list in ascending order
friends.reverse()  # reverses the order of the list
# friends.clear()  # removes all elements from the list
friends.extend(["Satya", "Satapal", "Satyarth"])
friends.index("Satya")  # returns the index of the first occurrence of "Satya"
friends.count("Satya")  # returns the number of occurrences of "Satya"
friends.copy()  # returns a shallow copy of the list
friends.sort(reverse=True)  # sorts the list in descending order
friends.reverse()  # reverses the order of the list again to get it back to ascending order
friends.insert(0, "Abhishek")  # inserts "Abhishek" at index 0
g= copy.deepcopy(friends)  # returns a deep copy of the list
print(f'deepcopy {g}')
h = copy.copy(friends)  # returns a shallow copy of the list
print(f'shallow copy {h}')
