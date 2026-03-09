def triangle_valid(A,B,C):
    if(A+B+C==180):
        return True
    return False

A = int(input("Enter the first angle in deegree :"))
B = int(input("Enter the second angles in deegree :"))
C = int(input("Enter the third angle in degree :"))

print(triangle_valid(A,B,C))