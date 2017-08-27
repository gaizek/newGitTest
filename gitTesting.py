import random
import sys
import os

pi_tuple = (3,1,4,1,5,9)

super_villains = {'Fiddler' : 'Isaac Bowin', 'Captain Cold' : 'Leonard Snart',
                    'Weather Wizard' : 'Mark McGoo'}

age = 16

if age >= 21 :
    print("You are old enough to drive a tractor")
elif age >= 16 :
    print("You are old enough to drive a car")
else :
    print("You are not old enough to drive")


newAge = 25
if((newAge >= 1) and (newAge <= 18)) :
    print("You are " + str(newAge) + " years old")
elif((newAge >= 21) or (newAge <= 65)) :
    print("You are old")


for x in range(0,10):
    print(x, end=" ")


print("\n")

grocery_list = ['Juice', 'Apples', 'Oranges', 'Grapes']
for x in grocery_list:
    print(x)
