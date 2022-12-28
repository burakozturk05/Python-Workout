# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:39:24 2022

@author: burak
"""
#%%
def factoriyel(x):
    if x == 1:
        return 1
    
    return x * factoriyel(x-1)
print(factoriyel(5))
#%%
def add_greetings(names):
    list = ["Hello"]
    for name in names:
        list.append("Hello, " + name)
        return list
print(add_greetings(["Burak", " Owen","Max"]))
#%%
def delete_starting_evens(lst):
    while (len(lst) > 0 (lst[0] % 2 == 0)):
        lst = lst[1:]
        return lst
#%%
#Exponents
def exponents(bases,powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst
print(exponents(2,3))
#%%
hobbies = ["swimming", "ping pong", "kung fu", "frisbee"]
count = 1
while count < len(hobbies) -1:
  print(hobbies[count])
  count+=1
#%%