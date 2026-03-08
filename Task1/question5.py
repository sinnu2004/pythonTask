def SI(p,r,t):
    return (p*r*t)/100

Principal = int(input("Enter the Principal :"))
Rate = int(input("Enter the Rate of Interest :"))
Time = int(input("Enter the Time in years: "))

print(SI(Principal,Rate,Time))