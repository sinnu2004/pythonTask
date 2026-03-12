# Write a program to calculate Simple Interest when Principal, Rate of Interest and Time
# Period are provided by the user.

def SI(p,r,t):
    return (p*r*t)/100   # SI = (Principal * Rate * Time)/100

Principal = int(input("Enter the Principal :"))
Rate = int(input("Enter the Rate of Interest :"))
Time = int(input("Enter the Time in years: "))

print(SI(Principal,Rate,Time))