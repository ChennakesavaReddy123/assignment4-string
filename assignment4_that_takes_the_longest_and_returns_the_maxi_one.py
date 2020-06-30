# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:46:31 2020

@author: Chennakesava Reddy
"""
#write apython prograsm that takes a list bif words and returns the longest one

a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("The word with the longest length is:")
print(temp)