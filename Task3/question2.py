
# WAP of start which increase first and then decrease

n = int(input("Enter the value :"))
def increase(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print("\n")

def decrease(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=" ")
        print("\n")
for i in range(1,n+1):
    if(i==n-1):
        increase(i)
    elif(i==n):
        decrease(i)
    else:
        continue