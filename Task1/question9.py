# Given two fractions, write a program to find their sum. Take the numerator and
# denominator of both fractions from the user.
def sum(a,b):
    return a + b

numerator1 = int(input("Enter the numerator for 1st fraction :"))
denomenator1 = int(input("Enter the denomenator for 2nd fraction :"))

numerator2 = int(input("Enter the numerator for 2nd fraction :"))
denomenator2 = int(input("Enter the denomenator for 2nd fraction :"))

if(denomenator1==0 or denomenator2==0):
    print("Denomenator can't be zero")

a = numerator1/denomenator1
b = numerator2/denomenator2

print(sum(a,b))
