# Q6. Factorial
# Find factorial of a given number using loop.
def fac(n):
    pro = 1
    for i in range(n,1,-1):
        pro = pro * i
    return pro

n = int(input("Enter the number :"))
print(fac(n))