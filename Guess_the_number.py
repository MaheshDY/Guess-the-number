# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:06:07 2021

@author: Mahesh DY
"""


import random

def guessnum(num):
    l=0
    h=1000000
    i=1
    while l<=h and i<50:
        mid=l+(h-l)//2
        i+=1
        if mid==num:
            return i
        elif mid >num:
            h=mid-1
        elif mid<num:
            l=mid+1

n=random.randint(1,1000000)
print("The guesses taken to guess the number {} are {}".format(n,guessnum(n)))
