# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 23:54:33 2022

@author: burak
"""
def f_to_c(f_temp):
  c_temp = (f_temp -32) * 5/9
  return c_temp
  f100_in_celsius = f_to_c(100)
print(f_to_c(100))

def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c_to_f(0))

def get_force(mass,acceleration):
  return mass * acceleration
train_force = get_force(22680,10)
print(train_force) 
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass,c):
  c = 3 * 10**8
  return mass * c
bomb_energy = get_energy(1,3 * 10**8)
print(bomb_energy)

print("A 1kg bomb supplies"+  str(bomb_energy)+ "Joules.")

def get_work(mass,acceleration,distance):
  return get_force(mass,acceleration) * distance
train_work = get_work(22680,10,100)
print(train_work)

print("The GE train does " + str(train_work)+ " Joules of work over "+ str(100)+ " meters.")


