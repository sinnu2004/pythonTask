
# Check whether string is symmetrical.
s = "naman"

i = 0
j = len(s)-1
flag = True
while(i<=j):
    if(s[i]!=s[j]):
        print("It is not Symmentrical")
        flag = False
        break
    i = i+ 1
    j = j -1
    

if(flag==True) :
    print("It is a symmentry")