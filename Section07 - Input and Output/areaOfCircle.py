#Using the math module:
import math

#PI = 3.1415

raio = float(input("Enter the radio of the circle in meters: "))

#area = PI * raio**2
area = math.pi * raio**2

print("The area of the circle is %.2f" %area + "m")