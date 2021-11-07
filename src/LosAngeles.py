# -*- coding: utf-8 -*-
'''
Created on 1 Nov. 2021

@author: jdvil
'''

import csv

from collections import namedtuple,defaultdict


'''
Remark: hood is a slang word that means neighborhood and 
because it is shorter we are going to use it sometimes.

'''
census = namedtuple('census','code,population,age,males,females,houses,houses_size,location,hood')

def leer_census(file):
    '''
    It gets a csv file route encoded in utf-8 and it returns a list of tuples with the 
    form of census(int,int,int,int,int,int,int,str,str) containing all the data stored in the file.
    '''
    res=list()
    with open(file,"r", encoding="utf-8") as f:
        lineas=csv.reader(f)
        next(lineas)    
        
        
        res=[census(int(code),int(population),int(age),int(males),int(females),int(houses),int(houses_size),location,hood)
             for code,population,age,males,females,houses,houses_size,location,hood in lineas]
            
    
    return res




     

     
     