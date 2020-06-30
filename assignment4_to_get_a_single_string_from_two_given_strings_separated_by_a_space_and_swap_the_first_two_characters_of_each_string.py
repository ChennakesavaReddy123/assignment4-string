# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:29:47 2020

@author:Chennakesava Reddy
"""

#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart')) 
