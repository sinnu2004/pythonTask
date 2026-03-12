# Q13. Arrange lowercase letters first in string.
s = "sssAAA bbBBBB"

i = 0
j = len(s)-1

while(i<=j):
    if(s[i]==' '):
        i = i + 1
    if(s[j]==' '):
        j = j - 1
    if(((ord(s[i]))>=97 and (ord(s[i]))<=122) and ((ord(s[j]))>=65 and (ord(s[j]))<=90)):
        temp = s[i] 
        s[i] = s[j]
        s[j] = temp
    elif((ord(s[i])>=97 and ord(s[i])<=122) and not(ord(s[j])>=65 and ord(s[j])<=90)):
        j = j - 1
    elif(not(ord(s[i])>=97 and ord(s[i])<=122) and (ord(s[j])>=65 and ord(s[j])<=90)):
        i = i+1

print(s)
        