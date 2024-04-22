import math
print("Calculating area of a Triangle")
#receive user input for three sides of a triangle
side1 = int(input("Enter side 1 : "))
side2 = int(input("Enter side 2 : "))
side3 = int(input("Enter side 3 : "))
s = (side1 + side2 + side3) / 2
print(s)
#calculate area of triangle
area = math.sqrt((s*(s-side1)*(s-side2)*(s-side3)))
#display results - area to user
print( "Area = ", area)
