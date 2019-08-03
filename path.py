# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 23:01:51 2019

@author: Pankaj
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Initialize data
node_value_data = np.genfromtxt("data.csv", delimiter="\t")
nodes = node_value_data.shape[0]
#Remove unknown value with Infinity
node_value_data[np.isnan(node_value_data)]  = np.Infinity

unvisited = [i for i in range(nodes)]
output = np.empty((0,3),int)

def findShortestPath(source,destination):
    global node_path_data,node_value_data,nodes,unvisited,visited,output
    
    for i in range(nodes):
        if i == source:
            output = np.vstack((output, np.array([i,0,0])))
        else:
            output = np.vstack((output, np.array([i,np.Infinity,-1])))
            
    while len(unvisited) != 0:
        min = np.Infinity
        current_node = np.Infinity
        
        for i in unvisited:
            if output[:,1][i] < min:
                min = output[:,1][i]
                current_node = i

        unvisited.remove(current_node)
                
        current_node_value = node_value_data[current_node]
        for i in range(nodes):
            if i in unvisited and current_node_value[i] != np.inf:
                if output[:,1][i] > (min+current_node_value[i]):
                    output[:,1][i] = min+current_node_value[i]
                    output[:,2][i] = current_node
    
    path = np.array([])
    i = destination                    
    while i != source:
        path = np.append(path,[i])
        i = int(output[:,2][i])
    path = np.append(path,[source])
    
    return np.flip(path)
        

print(findShortestPath(0,10))