# Create short form from initial letters.
s = "   saurabh prajapat"

if(s[0]!=' '):
    print(s[0].upper(),end=" ")
for i in range(1,len(s)):
    if(s[i-1]==' '):
        print(s[i].upper(),end=" ")
    else:
        continue
    

