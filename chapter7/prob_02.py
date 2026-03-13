#WRP to find out wether a student has passwed or failed if it require a total of 40% and atleast 33% in each subject to pass assume 3 subject and take marks as input from user

subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))


total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3
if average_marks >= 40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33:
    print("Congratulations! You have passed.")
else:
    print("Sorry, you have failed. Better luck next time!")