# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 22:30:56 2022

@author: burak
"""
lst = [3,4,5,6]
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

#^^33
print(append_sum(lst))
def larget_list(lst1,lst2):
    if len(lst1) > len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]
    
def more_than_n(lst,item,n):
    if lst.count(item) > n:
        return True
    else:
        return False
#print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

def combine_sort(lst1,lst2):
    unsorted = lst1 + lst2
    sortedList = sorted(unsorted)
    return sortedList

def every_three_nums(start):
    