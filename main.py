# Q1) Write a program that calculates the area of a triangle using the formula A = (b * h) / 2. The program should prompt the user to enter the base and height of the triangle and then display the calculated area.

Base = int(input("Enter the base of triangle: "))
Height = int(input("Enter the height of triangle: "))

Area = (Base * Height) / 2

print("The Area of triangle is:", Area)

# Q2) Write a program that prompts the user to enter two floating-point numbers and then calculate their average. The program should display the result with two decimal places.

num1 = float(input("Enter the value: "))
num2 = float(input("Enter the value: "))

avg = (num1 + num2) / 2

print("The average of", num1, "and", num2, "is {:.2f}".format(avg))

# Q3) Write a program that prompts the user to enter a radius and then calculates the volume and surface area of a sphere. The formulas for volume and surface area are V = (4/3) _ pi _ r^3 and A = 4 _ pi _ r^2, respectively.

radius = int(input("Enter the radius of a sphere: "))
pi = 3.142

Volume = 4/3 * pi * radius ** 3

Surface_Area = 4 * pi * radius ** 2

print("The volume of a sphere is", Volume)
print("The surface area of a sphere is", Surface_Area)
