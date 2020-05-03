# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:35:04 2020

@author: Hao
"""

import turtle

paper=turtle.Screen()
kai=turtle.Turtle()
kai.shape("turtle")

dist=2
accelaration=0.05
turn=20
steps=90

for _ in range(steps):
    kai.forward(dist)
    kai.right(turn)
    dist=dist*(1+accelaration)
    
paper.exitonclick()
