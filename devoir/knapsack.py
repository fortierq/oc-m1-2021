import matplotlib.pyplot as plt
import numpy as np
import time

def knapsack(C, objects):
    # à remplir
    # renvoyer la valeur maximum que l'on peut obtenir en prennant des objets dont le poids total est inférieur à C
    T=[[0 for c in range(0,C+1)] for i in range(0,len(objects)+1)]#Initialisation du tableau
    for i in range(1,len(objects)+1):#Pour tous les objets on va voir si ils sont dans les boites
        for c in range(0,C+1):
            if(c>=objects[i-1][0]):#Si on peut rajouter un objet 
                T[i][c]=max(T[i-1][c],T[i-1][c-objects[i-1][0]]+objects[i-1][1])#Max(La valeur de la capcité de l'objet précedent , objet précédent moins sa valeur plus valeur p=objet actuel
            else:
                T[i][c]=T[i-1][c]
    l=[]#Liste des objects à mettre
    capacity=C
    val=T[len(objects)][capacity]
    for i in range(len(objects),-1,-1):
        if(T[i][capacity]!=val):
            val-=objects[i][1]
            capacity-=objects[i][0]
            l.append(objects[i])
    return (T[len(objects)][C],l)
 
objects = [(2, 1), (3, 7), (6, 10), (5, 10), (8, 13), (2, 1), (2, 1)] # chaque objet est un couple (poids, valeur)
print(knapsack(10, objects)) # knapsack(10, objets) doit renvoyer 18
#Petit test sur la fonction pour voir si elle est pseudo-polynomiale

executionTime=[]
size=10_000
step=1000
inputSize=[i for i in range(0,size,step)]
capacity=20

for i in range(0,size,step):
    
    objectsList=list(map(tuple,np.random.randint(low=1,high=20, size=(i,2))))
    start=time.time()
    knapsack(capacity,objectsList)
    end=time.time()
    executionTime.append(end-start)

plt.plot(inputSize,executionTime)
plt.xlabel("inputSize",fontsize='13')
plt.ylabel("executionTime",fontsize='13')
plt.show()
