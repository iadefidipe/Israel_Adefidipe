# Code written by Israel Adefidipe
# written on the 24/03/2020
# A  program to that accepts a  user imputed radius as input and outputs the corresponding area
import math
print('Enter Desired radius(m): ')
Desired_radius = float(input()) # Input function returns string values which is converted to numerical value with the float()
Area = math.pi * Desired_radius ** 2
print('Area = ' + str(Area) + ' m²')
