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

def neighborhoods(census):
    '''
     It gets an ordered list of one of the fields with no repetition
    '''
    list1=[]
   
    
    for c in census:
        if c.hood in list1:
            pass
        else:
            list1.append(c.hood)
        
    return sorted(list1)

def sort_by_location(census,location):
    '''
    It gets a list of a field (hoods) in which 
    other field have to hold a condition (location). Location to try: beach, mountain and city
    '''
    aux=[]
    total_hoods=neighborhoods(census)
    for c in census:
        if c.location==location and c.hood not in aux:
            aux.append(c.hood)
    print("Number of neighborhoods in the",location+":",len(aux),"/",len(total_hoods))
    print("")       
    return sorted(aux)

def population_hood(census):
    
    '''
    It returns a dictionary which link two fields: for every neighborhood it sums the population 
    of every zip code  and the RESULT is a dictionary in which the key is the neighborhood and the value is the total population 
    of it
    '''
    aux=dict()
    hoods=neighborhoods(census)
    
    for h in hoods:
        population=0
        for c in census:
            if c.hood==h:
                population+=int(c.population)
        
        aux[h]=population
        
    return aux




     

     
     
