# write a program to print number pattern 

n = int(input("Enter the number :"))
for i in range(n,0,-1):   # reverse loop for reverse print
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")