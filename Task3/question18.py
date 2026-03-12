# Find uncommon words between two sentences.
s = "saurabh"
p = "prajapat"

common = ""
for i in range(len(s)):
    for j in range(len(p)):
        if(s[i]==p[j]):
            common = common + s[i]


common =  set(common)
print(common)


