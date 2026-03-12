# Conditional Sum
# Sum numbers from 1 to N, skip multiples of 5, stop if sum >300. Do not use for
def condi_sum(n):
    sum = 0
    i = 1
    while(i<n+1):
        if(i%5==0):
            i = i + 1
            continue
        elif(sum>300):
            break      
        else :
            sum = sum + i
        i = i + 1
    return sum

n = int(input("Enter the number :"))
print(condi_sum(n))