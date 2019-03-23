#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:51:09 2019

@author: susanlynch


Initialize all variables
"""
#principal_amount = 15000
principal_amount = int(input("Enter the starting amount of money "))
n = 12 # Number of times per year that interest will be calculated
r = 0.03875 # This is the interest rate

t = int(input("Enter the number of years "))
"""
Perform calculations

temp1 = n * t
temp2 = r/n
temp3 = 1 + temp2
temp4 = temp3 ** temp1

A = principal_amount * temp4
"""
A = principal_amount * (1+(r/n))**(n*t)
print("$"+str(A))
print("Amount is: $%7.2f" % (A))
