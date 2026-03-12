# Remove all characters except integers from a string.
s = "0002CD231068"
t = ""

for i in range(len(s)):
    if((ord(s[i])>=48 and (ord(s[i])<=57))):
        t = t + s[i]
    
    
s = t

print(s)
        