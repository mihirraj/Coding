# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 22:23:41 2018

@author: mihir
"""
import random

def power(x, y, p):
    return ((x**y)%p)

def millerTest(d, n):
    if(n > 4):
        a = 2 + (random.randint(2, n-2) % (n - 4))
        x = power(a, d, n)
        
        if(x == 1 or x == (n - 1)):
            return True
        while(d != n - 1):
            x = (x * x) % n 
            d *= 2
            if(x == 1):
                return False
            if(x == n - 1):
                return True
        return False
    
def isPrime(n, k):
    if(n <= 1 or n == 4):
        return False
    if(n <= 3):
        return True
    
    d = n - 1
    
    while(d % 2 == 0):
        d //= 2
        
    for i in range(k):
        if(not millerTest(d, n)):
            return False
    return True

k = 100
n = input("Enter a number greater than 1\n")
while(not n.isdigit() or int(n) <= 1):
    if(not n.isdigit()):
        print("Please input a number and not string!\n")
    else:
        print("Please input a number greater than 1 !\n")
    n = input("Enter a number greater than 1\n")
n = int(n)    
if(isPrime(n, k)):
    print("it is a prime number")
else:
    print("it is a composite number")    
        
        
        
    
            
                
            
    
