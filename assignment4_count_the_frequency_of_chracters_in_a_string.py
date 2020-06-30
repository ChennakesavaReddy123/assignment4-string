# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:27:26 2020

@author: Chennakesava Reddy
"""


#write apython program to count no of characters in a string
test_str= "gitamuniversity"
all_freq= {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("count of all characters in string is ;\n:"+str(all_freq))
