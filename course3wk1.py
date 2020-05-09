# -*- coding: utf-8 -*-
"""
Created on Fri May  8 20:08:09 2020

@author: Hao
"""


L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
for item in L:
    if 'hola' in item:
        test1=True
    else:
        test1=False
# Test if [5, 8, 7] is in the list L. Save to variable name test2
for item in L:
    print(item)
    if [5, 8, 7] == item:
        test2=True
    else:
        test2=False
    print(test2)
    
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data=False
for key in nested:
    if key=='data':
        data=True
        print(data)
    

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour=False
for k,v in nested.items():
    if key=='data':
        if 24 in v:
            twentyfour=True

        
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole=True
for k,v in nested.items():
    if key=='window':
        if 'whole' in v:
            whole=False
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics=False
for k,v in nested.items():
    if key=='physics':
        data=True



nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

for k,v in nested_d.items():
    if k=='London':
        london_gold=v['Great Britain']
        
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1=sports['swimming'][2]

# Assign the string 'platform' to the name v2
v2=sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3

v3=sports['gymnastics']['women']
# Assign the string 'rings' to the name v4
v4=sports['gymnastics']['men'][3]


nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}


US_count = []
for k,v in nested_d.items():
    for nk,nv in v.items():
        if nk=='USA':
            US_count.append(nv)



l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third=[]
for sub in l_of_l:
    third.append(sub[2])

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t=[]
other=[]

for sub in athletes:
    for item in sub:
        print(item)
        if 't' in item:
            t.append(item)
        else:
            other.append(item)






