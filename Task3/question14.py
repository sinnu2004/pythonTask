# Find sum and average of digits in an alphanumeric string.

s = "0002CD231068"
sum = 0
count = 0
for i in range(len(s)):
    if((ord(s[i])>=48 and (ord(s[i])<=57))):
        sum = sum + ord(s[i]) - 48
        count = count + 1
    
print(sum)
average = sum/count
print(average)