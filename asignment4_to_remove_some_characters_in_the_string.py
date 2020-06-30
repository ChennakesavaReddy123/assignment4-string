# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:14:33 2020

@author: Administrator
"""


#write a python program that takes alist of words and removes the nth one

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('Python', 0))
print(remove_char('Python', 2))
print(remove_char('Python', 5))
