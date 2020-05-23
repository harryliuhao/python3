# -*- coding: utf-8 -*-
"""
Created on Sat May 23 07:00:48 2020

@author: Hao
"""

class AppleBasket:
    def __init__(self, color,quantity):
        self.apple_color=color
        self.apple_quantity=quantity
    
    def increase(self):
        self.apple_quantity+=1
        
    def __str__(self):
        return 'A basket of {} {} apples.'.format(self.apple_quantity,self.apple_color)
        
        
a1=AppleBasket('yellow',10)
for i in range(10):    
    a1.increase()
print(a1)


class BankAccount:
    def __init__(self, name, amt):
        self.name=name
        self.amt=amt
     
    def __str__(self):
        return 'Your account, {}, has {} dollars.'.format(self.name, self.amt)

t1=BankAccount('BoB',100)
print(t1)