# ==============================
# LARGE SET CREATION
# ==============================

students = {
    "Abhishek", "Rahul", "Rohit", "Satyarth", "Shivam",
    "Anshul", "Priya", "Neha", "Amit", "Kunal",
    "Vikram", "Sneha", "Tanya", "Arjun", "Megha",
    "Riya", "Pooja", "Manish", "Dev", "Harsh",
    "Nikhil", "Yash", "Varun", "Aditya", "Aakash",
    "Raghav", "Ishaan", "Kartik", "Sahil", "Mohit",
    "Deepak", "Ritesh", "Sumit", "Naveen", "Aniket",
    "Sandeep", "Gaurav", "Tarun", "Bhavesh", "Lokesh",
    "Chirag", "Pranav", "Rohini", "Komal", "Divya",
    "Aishwarya", "Shreya", "Simran", "Anjali", "Nandini",
    "Muskan", "Kritika", "Sakshi", "Palak", "Isha",
    "Radhika", "Tanvi", "Mansi", "Juhi", "Khushi",
    "Ayush", "Lakshya", "Parth", "Dhruv", "Vivaan",
    "Krishna", "Aryan", "Shaurya", "Om", "Atharv",
    "Vedant", "Pratham", "Aarav", "Reyansh", "Vihaan",
    "Kabir", "Rudra", "Shlok", "Arnav", "Yuvraj",
    "Devansh", "Ayaan", "Harshit", "Prateek", "Ujjwal",
    "Hemant", "Saurabh", "Tushar", "Kapil", "Abhay",
    "Mayank", "Rajat", "Vikas", "Sameer", "Akash",
    "Tejas", "Manav", "Keshav", "Nitin", "Piyush",
    "Chandan", "Raman", "Samar", "Nakul", "Jay",
    "Siddharth", "Anirudh", "Ravi", "Karan", "Suraj",
    "Vivek", "Himanshu", "Ashish", "Ajay", "Dinesh"
}

print("Total Students:", len(students))

print("Original Set:", students)


# =====================================================
# 🔥 TOP 7 MUST-KNOW SET METHODS (Most Important)
# =====================================================

# 1️⃣ add() → Add single element
temp = students.copy()
temp.add("Riya")
print("\nAfter add():", temp)


# 2️⃣ update() → Add multiple elements
temp = students.copy()
temp.update(["Pooja", "Manish"])
print("\nAfter update():", temp)


# 3️⃣ remove() → Remove element (Error if not found)
temp = students.copy()
temp.remove("Rahul")
print("\nAfter remove():", temp)


# 4️⃣ discard() → Remove safely (No error if not found)
temp = students.copy()
temp.discard("Unknown")
print("\nAfter discard():", temp)


# 5️⃣ pop() → Remove random element
temp = students.copy()
popped = temp.pop()
print("\nPopped element:", popped)
print("After pop():", temp)


# 6️⃣ union() → Combine sets
set2 = {"Riya", "Kunal", "Dev"}
print("\nUnion:", students.union(set2))


# 7️⃣ intersection() → Common elements
print("\nIntersection:", students.intersection(set2))


# =====================================================
# ⚡ SECOND PRIORITY METHODS
# =====================================================

# 8️⃣ difference() → Elements in students not in set2
print("\nDifference:", students.difference(set2))


# 9️⃣ symmetric_difference() → Elements in either but not both
print("\nSymmetric Difference:", students.symmetric_difference(set2))


# 1️⃣0️⃣ issubset()
small_set = {"Abhishek", "Rahul"}
print("\nIs subset:", small_set.issubset(students))


# 1️⃣1️⃣ issuperset()
print("\nIs superset:", students.issuperset(small_set))


# 1️⃣2️⃣ isdisjoint()
set3 = {"X", "Y"}
print("\nIs disjoint:", students.isdisjoint(set3))


# =====================================================
# 🧠 BASIC OPERATIONS (Important Concepts)
# =====================================================

# Length
print("\nLength of set:", len(students))

# Membership check
print("Is 'Rahul' in set?", "Rahul" in students)

# Copy
copy_set = students.copy()
print("Copied Set:", copy_set)

# Clear
temp = students.copy()
temp.clear()
print("After clear():", temp)


# =====================================================
# 🚀 OPERATORS (Very Important in Interviews)
# =====================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nUnion using | :", A | B)
print("Intersection using & :", A & B)
print("Difference using - :", A - B)
print("Symmetric Difference using ^ :", A ^ B)


# =====================================================
# ⚠️ IMMUTABLE SET (FROZENSET)
# =====================================================

frozen = frozenset([1, 2, 3, 4])
print("\nFrozen Set:", frozen)

# frozen.add(5)  # ❌ This will give error (immutable)