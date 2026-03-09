def reverse_int(n):
    sum = 0
    while(n>0):
        r = n%10
        sum = sum * 10 + r
        n = n//10
    return sum

n = int(input("Enter the number :"))
print(reverse_int(n))