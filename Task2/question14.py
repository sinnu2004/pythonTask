# Q14. Armstrong Numbers
# Print all Armstrong numbers in a given range.
def count(n):
    count = 0
    while(n>0):
        r = n%10
        count = count + 1
        n = n//10
    return count

def armstrong(n):
    power = count(n)
    sum = 0
    while(n>0):
        r = n%10
        sum = sum + r**power
        n = n//10
    return sum

n = int(input("Enter the number :"))
if(armstrong(n)==n):
    print("It is Armstrong Number")
else:
    print("It is not a Armstrong Number")