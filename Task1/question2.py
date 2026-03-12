# Q2. Write a Python program that converts temperature from Celsius to Fahrenheit.
# Formula: Fahrenheit = (Celsius × 9/5) + 32

def convert(n):
    return (n*9/5) + 32  # formula to convert the celsius to fahrenheight

celsius = int(input("Enter the Celcius deegree: "))

Fahrenheit = convert(celsius)
print(Fahrenheit)