# -*- coding: utf-8 -*-
'''
Created on 1 Nov. 2021

@author: josodommor3

Remark: hood is a slang word that means neighborhood and 
because it is shorter we are going to use it sometimes.

'''
from LosAngeles import *

census=leer_census('../data/census_population.csv')

def leer_censusTEST():
	print(census[0:2])
	print(census[-3:-1])
	print(len(census))



leer_censusTEST();
