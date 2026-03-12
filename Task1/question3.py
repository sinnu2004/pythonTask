# Take two numbers as input from the user and write a program to swap the numbers
# without using any special Python syntax.
a = int(input("Enter the 1st number :"))  # taking inputs
b = int(input("Enter the 2nd number :"))
print(a,b)

a,b = b,a  # swapping to numbers 

print(a,b)