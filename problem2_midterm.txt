#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:46:50 2020

@author: NorinaSun
"""
import pandas as pd 

graph_matrix = pd.DataFrame([[0,6,4,0,0,0,0,0,0],
                            [6,0,0,5,6,0,0,0,0],
                            [4,0,0,5,0,0,2,0,0],
                            [0,5,5,0,0,5,3,0,0],
                            [0,6,0,0,0,4,0,5,0],
                            [0,0,0,5,4,0,0,3,4],
                            [0,0,2,3,0,0,0,0,2],
                            [0,0,0,0,5,3,0,0,5],
                            [0,0,0,0,0,4,2,5,0]],
                            index=['A','B','C','D','E','F','G','H','I'],
                            columns=['A','B','C','D','E','F','G','H','I'])


class Node:
    def __init__(self,node):
        self.id = node
        self.capacity = float('-inf')
        self.path = [node]
        self.visited = False
        

Node_A = Node("A")
Node_A.capacity = float('inf')
Node_B = Node("B")
Node_C = Node("C")
Node_D = Node("D")
Node_E = Node("E")
Node_F = Node("F")
Node_G = Node("G")
Node_H = Node("H")
Node_I = Node("I")

Node_Dict = {'A':Node_A,'B':Node_B,'C':Node_C,'D':Node_D,'E':Node_E,'F':Node_F,'G':Node_G,'H':Node_H,'I':Node_I}

def update_capacities(current,Node_Dict):
    for node in Node_Dict:
        vertex_value = graph_matrix.loc[current,node]
        if vertex_value > 0:
            new_path_value = min(Node_Dict[current].capacity,vertex_value)
            old_path_value = Node_Dict[node].capacity
            Node_Dict[node].capacity =  max(new_path_value, old_path_value)
            if new_path_value > old_path_value:
                Node_Dict[node].path = [node]
                Node_Dict[node].path = Node_Dict[current].path + Node_Dict[node].path    
    Node_Dict[current].visited = True
    del Node_Dict[current]
    return Node_Dict
            

def determine_max(Node_Dict):
    current_max = 0
    for node in Node_Dict:
        if Node_Dict[node].capacity > current_max:
            current_max = Node_Dict[node].capacity
            chosen_node = node
    return chosen_node

def run_algo(Node_Dict):
    Node_Dict_Instance = Node_Dict.copy()
    while bool(Node_Dict_Instance) == True:
        current = determine_max(Node_Dict_Instance)
        Node_Dict_Instance = update_capacities(current,Node_Dict_Instance)
    Node_A.capacity = 0
        
if __name__ == "__main__":
    
    run_algo(Node_Dict)
    
    for node in Node_Dict:
        print("Node: ",node," Node Capacity: ",Node_Dict[node].capacity," Optimal ZPath from A: ",Node_Dict[node].path)
        
        
        
    
