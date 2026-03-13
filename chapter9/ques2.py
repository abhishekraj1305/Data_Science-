#WRP To convert temperature from Celsius to Fahrenheit and vice versa


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")
if unit.upper() == 'C':
    print(f"{temp}°C is equal to {celsius_to_fahrenheit(temp)}°F")
elif unit.upper() == 'F':
    print(f"{temp}°F is equal to {fahrenheit_to_celsius(temp)}°C")
else:
    print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
    