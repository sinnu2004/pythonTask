# Q5. Sum of series: 1 + x^2/2 + x^3/3 + ... + x^n/n
def sumOfSeries(n,x):
    sum = 1
    for i in range(2,n+1):
        sum = sum + (x**i)/i
    return sum

n = int(input("Enter the number of terms :"))
x = int(input("Enter the value of x :"))

print(sumOfSeries(n,x))