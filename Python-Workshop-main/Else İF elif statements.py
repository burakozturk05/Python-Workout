# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 22:27:38 2022

@author: burak
"""
#%%
#Workout 1
def large_power(base,exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False
#Workout 2
def over_budget(budget,food_bill,electricity_bill,internet_bill,rent):
    if budget < (food_bill + electricity_bill + internet_bill + rent):
        return True
    else:
        return False

#Workout 3

def twice_as_large(num1,num2):
    if num1  > num2 * 2:
        return True
    else:
        return False
#Workout 4
def divisible_by_ten(num):
    if (num % 10 == 0):
        return True
    else:
        return False
#Workout 5
def not_sum_to_ten(num1,num2):
    if (num1 + num2) != 10:
        return True
    else:
        return False
print(not_sum_to_ten(-1, 9))
#%% 
# CONTROL FLOW ADVANCED
def in_range(num,lower,upper):
    if (num >= lower) and (num <= upper):
        return True
    else:
        return False
bmw = in_range(3,5,7)
def same_name(your_name, my_name):
    if (your_name == my_name):
        return True
    else:
        return False
    print(same_name(Colby,Colby))
def always_false(num):
    if (num > 0 and num < 0):
        return True
    else:
        return False
print(always_false(5))
#%%
def max_num(num1,num2,num3):
    if (num1 > num2) and (num1 > num3):
        return num1
    elif (num2 > num1) and (num2 > num3):
        return num2
    elif (num3 > num1) and (num3 > num2):
        return num3
    else:
        return"Its a tie"
print(max_num(5, 2, 5))
    

    
    