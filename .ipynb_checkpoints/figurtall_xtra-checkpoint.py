#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:08:54 2021

@author: elisabethengum
"""

def figurtall(n):
    return n**2 - n + 1

sum = 0

antall = int(input("Hvor mange figurer ønsker du å lage? "))

for i in range(1,antall+1,1):
    sum += figurtall(i)
    
    
print(f"For å lage {antall} figurer, så må du tegne {sum} prikker totalt")