# Reverse words in a sentence.

s = "saurabh"
t = ""

for i in range(len(s)-1,-1,-1):
    t = t + s[i]

s = t
print(s)