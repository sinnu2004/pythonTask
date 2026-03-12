# Hcf and Lcm of a number

def Hcf(a,b):
    res = 0
    while(b!=0):
        if(a%b==0):
            res = b
            break
        else:
            a,b = b,a%b
    return res

a = int(input("Enter the value of first number :"))
b = int(input("Enter the value of second number :"))

hcf = Hcf(a,b)
Lcm = ((a*b)/hcf)

print(hcf,Lcm)
