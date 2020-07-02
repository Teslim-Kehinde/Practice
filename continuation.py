# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 07:30:11 2020

@author: KEHINDE TESLIM
"""



def add(x,y): 
    return(x+y)
    
def addd(func,x,y):
    return func(func(x,y),func(x,y))

a=int(input("Enter a number: "))
b=int(input("Enter second number: "))
plus = add
print(addd(plus,a,b))
