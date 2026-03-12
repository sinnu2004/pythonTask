# Decimal to binary

def DtoB(n):
    num = 0
    i = 0
    li = []
    while(i<n):
        r = n%2
        li.append(r)
        n = n//2
    return li


n = int(input("Enter the number :"))

binary = DtoB(n)
binary.reverse()
print(binary)


