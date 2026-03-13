#wrp to accept marks of 6 students and display them in sorted manner
marks = []

f1 = int(input("Enter the marks of a student: "))
marks.append(f1)
f2 = int(input("Enter the marks of a student: "))
marks.append(f2)
f3 = int(input("Enter the marks of a student: "))
marks.append(f3)
f4 = int(input("Enter the marks of a student: "))
marks.append(f4)
f5 = int(input("Enter the marks of a student: "))
marks.append(f5)
f6 = int(input("Enter the marks of a student: "))
marks.append(f6)
f7 = int(input("Enter the marks of a student: "))
marks.append(f7)

marks.sort()
print("The sorted marks of the students are: ", marks)