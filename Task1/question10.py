# Q10. Given the height, length and breadth of a milk tank, calculate how many glasses of milk
# can be obtained.

length = int(input("Enter the Length of the tank :"))
breadth = int(input("Enter the breadth of the tank :"))
height = int(input("Enter the height of the tank :"))

radius = int(input("Enter the radius of the glass :"))
height_glass = int(input("Enter the height of the glass :"))
volume_of_tank = length * breadth * height
pi = 3.14
volume_of_glass =  pi * radius**2 * height_glass

Glasses_of_milk = volume_of_tank/volume_of_glass

print(Glasses_of_milk)