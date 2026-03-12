# Fibonacci Series
# Display Fibonacci series up to 10 terms.
def fibo(n):
    pre = 0
    curr = 1
    print(pre)
    print(curr)
    for i in range(2,n+1):
        term = pre + curr
        print(term)
        pre = curr
        curr = term

n = int(input("Enter the number of terms :"))
fibo(n)