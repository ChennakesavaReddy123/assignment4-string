# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:40:36 2020

@author: Chennakesava Reddy
"""

#write a python program to get a string where all occrrences of its first char havebeen changed to"$",except the first char itself

def v(str1):
    c= str1[0]
    str1= str1.replace(c,'$')
    str1= c+str1[1:]
    
    return str1
print(v('restart'))