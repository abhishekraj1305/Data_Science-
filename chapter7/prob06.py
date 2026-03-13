#WRP to calculate grade of student from his marks from follwing scheme 
# 90-100 Ex
# 80-90 A
# 70-80 B
# 60-70 C
# 50-60 D
# >= 50 F


marks = float(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Grade: Ex")
elif marks >= 80 and marks < 90:
    print("Grade: A")
elif marks >= 70 and marks < 80:
    print("Grade: B")
elif marks >= 60 and marks < 70:
    print("Grade: C")
elif marks >= 50 and marks < 60:
    print("Grade: D")
elif marks >= 0 and marks < 50:
    print("Grade: F")
else:
    print("Invalid marks entered. Please enter marks between 0 and 100.")