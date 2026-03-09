def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            print("it is not a prime number")
            return False
    return True


n = int(input("Enter the number :"))
print(is_prime(n))


