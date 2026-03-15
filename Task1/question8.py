# Q8. Given the first two terms of an Arithmetic Series, write a program to find the Nth term
# of the series. Assume all inputs are provided by the user.

def ArithmeticSeries(b,d,n,curr):
    while(curr!=n):
        b = b + d
        curr += 1
    return b
a = int(input("Enter the 1st term :"))
b = int(input("Enter the 2nd term :"))

diff = b - a
n = int(input("Enter the Nth term required :"))
print(ArithmeticSeries(b,diff,n,2))

result = a + (n-1)*diff
print(result)
