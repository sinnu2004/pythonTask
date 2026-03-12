# Write a Python program to calculate the Euclidean distance between two coordinates.
# Take (x1, y1) and (x2, y2) as input from the user.

x1 = int(input("Enter the 1st x coordinate :"))
y1 = int(input("Enter teh 1st y coordinate :"))

x2 = int(input("Enter the 2nd x coordinate :"))
y2 = int(input("Enter the 2nd y coordinate :"))

Euclian_distance = ((x2-x1)**2 + (y2-y1)**2)**0.5  # Euclian distance formula

print(Euclian_distance)