# Write a program that determines the number of dogs and chickens when the user
# provides the total number of heads and legs.
# Example: Heads = 4, Legs = 12 → Dogs = 2, Chickens = 2

h = int(input("Enter the number of heads :"))

l = int(input("Enter the number of legs :"))

# c + d = h
# 2c + 4d = l

d = (l-2*h)//2
c = (4*h-l)//2


# d = l//2 - h
# c = h - d

if(h>0 and l>0 and 2*c + 4*d ==l):
    print("Dogs:",d)
    print("Chickens :",c)
else:
    print("Not Possible")
