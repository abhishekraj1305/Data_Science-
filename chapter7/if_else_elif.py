#if elif else detailed branching in python

age = int(input("Enter your age: "))

if age>= 100:
    print("You are a centenarian.")
elif age >= 90:
    print("You are a nonagenarian.")
elif age >= 80:
    print("You are an octogenarian.")
elif age >= 70:
    print("You are a septuagenarian.")
elif age >= 60:
    print("You are a sexagenarian.")
elif age >= 50:
    print("You are a quinquagenarian.")
elif age >= 40:
    print("You are a quadragenarian.")
elif age >= 30:
    print("You are a tricenarian.")
elif age >= 20:
    print("You are a vicenarian.")
elif age >= 10:
    print("You are a decenarian.")
else:
    print("You are a child.")