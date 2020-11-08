#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:39:01 2020

@author: NorinaSun
"""
a_one = 0
a_two = 0
b_one = 0
b_two = 0
x = 0


def algo(a_one,b_one,a_two,b_two,x):
    counter = 0
    print("iteration: ",counter)
    e = 1e-8
    
    y_one = a_one*x + b_one
    y_two = a_two*x + b_two
    print("y_one: ",y_one)
    print("y_two: ",y_two)
    
    while abs(y_one - y_two) > e:
        counter += 1
        print("iteration: ",counter)
        y = (y_one+y_two)/2
        print("y: ",y)
        x_one = (y-b_one)/a_one
        x_two = (y-b_two)/a_two
        print("x_one: ",x_one)
        print("x_two: ",x_two)
        x = (x_one + x_two)/2
        print("x: ",x)
        y_one = a_one*x + b_one
        y_two = a_two*x + b_two
        print("y_one: ",y_one)
        print("y_two: ",y_two)
        
    y = (y_one+y_two)/2
    return x,y


print(algo(1,2,2,4,1))
    
    