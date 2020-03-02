# Case Study I: Module3–Deep Dive -Functions, OOPs, Modules, Errors and Exceptions

# Problem 1
# 1.A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT. 
# The trace of Robot movement is as given following:UP 5DOWN 3LEFT 3RIGHT 2The numbers after directions are steps.  
# Write a program to compute the distance current position after sequence of movements.
# Hint: Use math module.

import math

x, y = 0, 0

while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)

# Problem 2
# 2.Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
# Hint: Use if/elif to deal with conditions.

sorted_list = ['a', 'b', 'c', 'd']
data = input("Enter data:")

if data in sorted_list:
    print(data)
else:
    print(data,"is not in list.")

# Problem 3
# 3.Weather forecasting organization wants to show is it day or night. So, write a program for such organization to findwhether is it dark outside or not.
# Hint: Use time module.

import time
from time import struct_time

current_time = time.struct_time(time.localtime())


if current_time.tm_hour < 12:
    print('This is Day')
elif current_time.tm_hour > 4 and current_time.tm_hour < 7:
    print('This is Evening')
else:
    print('This is Night')

# Problem 4
# 4.Write a program to find distancebetween two locations when their latitude and longitudes are given.
# from math import radians, cos, sin, asin, sqrt
# Hint: Use math module.

from math import radians, cos, sin, asin, sqrt 
def distance(lat1, lat2, lon1 ,lon2):
    # convert degree to radiant 
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1)* cos(lat2)* sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # radius of earth in kilometers. Use 3956 for miles
    r = 6371
    #caliculate the result
    return(c*r)

#derive code
lat1 = 53.3205555555
lat2 = 53.3186111111
lon1 = -1.7297222222
lon2 = -1.6997222222
print(distance(lat1,lat2,lon1,lon2))


#Problem 5 
# 5.Design a software for bank system. There should be options like cash withdraw, cash credit and change password. 
# According to user input, the software should provide required output.
# Hint: Use if else statements and functions.

print("Options:""\n""1- Cash withdraw""\n""2- Cash credit""\n""3- Change password")
option = int(input("Enter the your option:"))

default_cash = 2000
default_pass = 'test123'


def cash_withdraw():
    print('How much cash do you want to withdraw?')
    wd_cash = int(input())
    if default_cash >= wd_cash:
        remaning_cash = int(default_cash - wd_cash)
        print("You have successfully removed",wd_cash,"amount.")
        print("Your current balance is ",remaning_cash,"amount.")
    else:
        print("You dont have sufficient balance.")

def cash_credit():
        print("How much cash do you want to credit?")
        cr_cash = int(input())
        total_cash = default_cash + cr_cash
        print("You have succesfully added ",cr_cash," to your account.")
        print("Now your current balance is ",total_cash,".")

def change_pass(default_pass):
        print("Enter your password:")
        default_pass1 = default_pass
        chang_pass = str(input())
        if chang_pass != default_pass1:
            default_pass1 = chang_pass
            print('Password change successfully to: ', default_pass1)
            return(default_pass1)
        else:
            print('password not updated')
            return(default_pass1)
  

if (option==1):
    cash_withdraw()
elif(option == 2):
    cash_credit()
elif(option == 3):
    default_pass = change_pass(default_pass)
    print(default_pass)
else:
    print("Not a valid option, Please select the valid option from above.")



