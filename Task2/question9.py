sum = 0
count = 0
n = int(input("Enter the number :"))
while(n>0):
    sum = sum + n
    count = count + 1
    avg = sum/count
    print("Enter zero if you want to stop!")
    n = int(input("Enter the number :"))
    
print(sum,avg)