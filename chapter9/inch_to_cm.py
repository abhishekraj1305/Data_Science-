#WRP Inch to cm converter

def inch_to_cm(inches):
    return inches * 2.54

inches = float(input("Enter the length in inches: "))
cm = inch_to_cm(inches)
print(f"The length of {inches} inches in centimeters is: {cm}")