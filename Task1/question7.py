# Write a program to find the sum of squares of the first n natural numbers where n is
# provided by the user.
def sos(n):
    return n*(n+1)*(2*n+1)/6   # formula of sum of square of natural number

n = int(input("Enter the number :"))
print(sos(n))