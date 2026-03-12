# series sum of 2 + 22 + 222 + 2222...

def series(n):
    sum = 2
    num = 2
    print(num,end=" ")
    for i in range(2,n+1):
        num = num * 10 + 2
        print(num,end=" ")
        sum = sum + num
    print("\n")
    return sum

n = int(input("Enter the number of terms :"))
print(series(n))
