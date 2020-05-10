# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:46:57 2020

@author: Hao
"""

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing=map(lambda x: 'Fruit: '+x, lst_check)
print(map_testing)

test=[2,3,5]
test1=map(lambda x: x*2,test)
print(test1)

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries=filter(lambda c: c[0]=='B',countries)

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

people[0][1]
first_names=[n[1] for n in people]

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2=[e*2 for e in lst]

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed=[s[0] for s in students if s[1]>=70]

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

opposites=[(x1, x2) for (x1, x2) in zip(l1,l2) if len(x1)>3 and len(x2)>3]
opposites=filter(lambda n: len(n[0])>3 and len(n[1])>3, zip(l1,l2))
opposites=list(filter(lambda n: len(n[0])>3 and len(n[1])>3, zip(l1,l2)))
test=list(filter(lambda n: len(n[0])>3, list(zip(l1,l2))))


species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info=zip(species,population)
endangered=[x for x in pop_info if x[1]<2500]