import random
import sys
import os


print("This program calculates MPG")
miles_driven = input("Enter miles driven: ")
miles_driven = float(miles_driven)
gallons_used = input("Enter gallons used: ")
gallons_used = float(gallons_used)
mpg = miles_driven / gallons_used
print("Miles per gallon: ", mpg)
