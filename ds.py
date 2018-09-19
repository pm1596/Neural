'''
def create_matrix(m, n):
    return [[0]*n for _ in range(m)]

a = create_matrix(8, 8)
print(a)
'''
from fileinput import filename
from _ast import Store

'''
import random;
from numpy.random import sample

random .sample(range(1,9999),1000)
'''


'''
import random
from random import randint
print(randint(0,9))

def create_matrix(m,n):
    return [[randint(0,9)]*n for _ in range(m)]
a = create_matrix(8, 8)

#nums = [x for x in range(10)]

for i in range(0,1):
    random.shuffle(a)
    print(a)
''' 
    


'''
import random
nums = [x for x in range(10)]
random.shuffle(nums)
print(nums)
'''
'''
import numpy

def weighted_adjmatrix(adjlist, nodes):
    Returns a (weighted) adjacency matrix as a NumPy array.
    matrix = []
    for node in nodes:
        weights = {endnode:int(weight)
                   for w in adjlist.get(node, {})
                   for endnode, weight in w.items()}
        matrix.append([weights.get(endnode, 0) for endnode in nodes])
    matrix = numpy.array(matrix)
    return matrix + matrix.transpose()
'''
'''
import random

def random_adjacency_matrix(n):   
    matrix = [[random.randint(0, 1) for i in range(5)] for j in range(5)]

    # No vertex connects to itself
    for i in range(5):
        matrix[i][i] = 0

    # If i is connected to j, j is connected to i
    for i in range(5):
        for j in range(5):
            matrix[j][i] = matrix[i][j]

    return matrix
#print(random_adjacency_matrix(n))
'''
import os
import numpy as np
import random
from random import randint
def graph_input():
    V = random.randint(1,10)
    E = random.randint(0,9)

    print (V)

    adj_matrix = []
 # vertex numbering starts from 0
    for i in range(0, V):
        
        temp = []
        for j in range(0, V):
            temp.append(0)
        adj_matrix.append(temp)
    
    for i in range(0, E):
        
        for u in range(0,V):
            for v in range(0,V):
                if (u==v):
                    adj_matrix[v][u] = adj_matrix[u][v] = 0
                else:
                    
                    adj_matrix[v][u] = adj_matrix[u][v] = randint(0,9)
        
        

 # print the adjacency matrix
    for i in range (0, V):
        print (adj_matrix[i])
    print ("---------------------------------")
   # return adj_matrix

    for u in range(0,V):
        for v in range(0,V):
            
            if(adj_matrix[v][u] == adj_matrix[u][v] == 0):
                
                adj_matrix[v][u] = adj_matrix[u][v] = 0
            else:
                adj_matrix[v][u] = adj_matrix[u][v] = 1
                
        for i in range (0, V):
            print (adj_matrix[i])
        print ("-------------------------------")
        
   
             
              
    result=np.array(adj_matrix)
    print (result)

    
    
    for i in range (0,V):
        data = [result[i]]
        out = csv.writer(open("E:/dataset.csv","a"), delimiter=",",quoting=csv.QUOTE_ALL)
        out.writerow(data)
    
graph = graph_input()
