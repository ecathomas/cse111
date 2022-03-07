import math
width = int(input('Enter the width of the tire is mm: '))
aspect = int(input('Enter the aspect ratio of the tire: '))
diameter = int(input('Enter the diameter of the wheel in inches: '))

volume = (math.pi *(width**2)*aspect*((width*aspect)+(2540*diameter)))/10000000000

print (f'\nThe approximate volume is {volume:.2f} liters')