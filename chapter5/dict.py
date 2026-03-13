#dictionary


# print(mark["Abhishek"])  # Output: 90
# print(mark["Rahul"])  # Output: 85
# print(mark["Rohit"])  # Output: 80
# print(mark["Satyarth"])  # Output: 95

# print(mark.get("Shivam"))  # Output: 88

# print(mark,type(mark))  # Output: {'Abhishek': 90, 'Rahul': 85, 'Rohit': 80, 'Satyarth': 95, 'Shivam': 88, 'Anshul': 92} <class 'dict'>



# #Dictionary methods
# mark["Abhishek"] = 91  # Update the value for the key "Abhishek"
# mark["Satya"] = 89  # Add a new key-value pair to the dictionary
# print(mark)  # Output: {'Abhishek': 91, 'Rahul': 85, 'Rohit': 80, 'Satyarth': 95, 'Shivam': 88, 'Anshul': 92, 'Satya': 89}
# print(mark.keys())  # Output: dict_keys(['Abhishek', 'Rahul', 'Rohit', 'Satyarth', 'Shivam', 'Anshul', 'Satya'])
# print(mark.values())  # Output: dict_values([91, 85, 80,95, 88, 92, 89])
# print(mark.items())  # Output: dict_items([('Abhishek', 91),
# # ('Rahul', 85), ('Rohit', 80), ('Satyarth', 95), ('Shivam', 88), ('Anshul', 92), ('Satya', 89)])
# print(mark.get("Abhishek"))  # Output: 91
# print(mark.get("Rahul"))  # Output: 85
# print(mark.get("Rohit"))  # Output: 80
# print(mark.get("Satyarth"))  # Output: 95
# print(mark.get("Shivam"))  # Output: 88
# print(mark.get("Anshul"))  # Output: 92
# print(mark.get("Satya"))  # Output: 89
# print(mark.get("NonExistentKey", "Default Value"))  # Output: "Default Value"

# mark.pop("Satya")  # Remove the key "Satya" and its associated value from the dictionary
# print(mark)  # Output: {'Abhishek': 91, 'Rahul':    85, 'Rohit': 80, 'Satyarth': 95, 'Shivam': 88, 'Anshul': 92}
# mark.popitem()  # Remove the last key-value pair added to the dictionary
# print(mark)  # Output: {'Abhishek': 91, 'Rahul': 85, 'Rohit': 80, 'Satyarth': 95, 'Shivam': 88}
# # mark.clear()  # Remove all key-value pairs from the dictionary
# mark.update({"Abhishek": 92, "Rahul": 86, "Renuka":98, 'Shyam':100, 'Rohan':78})# Update the values for the keys "Abhishek" and "Rahul"
# print(mark)  # Output: {'Abhishek': 92, 'Rahul': 86, 'Rohit': 80, 'Satyarth': 95, 'Shivam': 88, 'Renuka': 98, 'Shyam': 100, 'Rohan': 78}


# print(mark.get("Abhineet"))  # Output: 92
# print(mark["Abhineet"])  # Output: error because we cannot call a dictionary like a function

mark = {
    "Abhishek": 90,
    "Rahul": 85,
    "Rohit": 80,
    "Satyarth": 95,
    "Shivam": 88,
    "Anshul": 92,
    "Priya": 91,
    "Neha": 87,
    "Amit": 78,
    "Kunal": 83,
    "Vikram": 89,
    "Sneha": 94,
    "Tanya": 86,
    "Arjun": 82,
    "Megha": 93
}

print("Keys:", mark.keys())
print("Values:", mark.values())
print("Items:", mark.items())
for name, score in mark.items():
    print(name, "scored", score)
    
print("Rahul's Marks:", mark.get("Rahul"))
print("Unknown Student:", mark.get("Unknown", "Not Found"))

mark.update({"Abhishek": 99})
mark.update({"Riya": 84})

print("After Update:", mark)

removed = mark.pop("Amit")
print("Removed:", removed)
print("After Pop:", mark)

temp_dict = mark.copy()
temp_dict.clear()
print("After Clear:", temp_dict)

copy_dict = mark.copy()
print("Copied Dictionary:", copy_dict)

temp = mark.copy()
print("Popped Item:", temp.popitem())
print("After popitem:", temp)

mark.setdefault("NewStudent", 70)
print("After setdefault:", mark)

students = ["A", "B", "C"]
new_dict = dict.fromkeys(students, 0)
print("Fromkeys:", new_dict)

print("Rahul in dictionary?", "Rahul" in mark)

temp = mark.copy()
del temp["Rahul"]
print("After del:", temp)

print("Length:", len(mark))

sorted_dict = dict(sorted(mark.items(), key=lambda x: x[1]))
print("Sorted by Marks:", sorted_dict)