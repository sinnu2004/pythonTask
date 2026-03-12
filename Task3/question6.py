# Q6. Calculate first seven terms of logarithmic series.
import math

def logrithm(n):
    
    for i in range(1,n+1):
        print(math.log(i),end=",")

n = int(input("Enter the number :"))
logrithm(n)