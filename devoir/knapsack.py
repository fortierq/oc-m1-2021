#En stockant toutes les valeurs
def knapsack1(C, objects): 
    n = len(objects) + 1 # +1 pour pouvoir accéder à l'élement n, pareil pour C
    v = [ [0]*n for i in range(C+1)]
    for k in range(1, n):
        for c in range(C+1):
            if (c-objects[k-1][0]>=0) :
                v[c][k] = max(v[c][k-1], (v[c-objects[k-1][0]][k-1] + objects[k-1][1]))
            else :
                v[c][k] = v[c][k-1]
    return v[c][k]  

#En stockant uniquement la valeur précedente
def knapsack2(C, objects): 
    n = len(objects) + 1
    v = [ 0*n for i in range(C+1)]
    for k in range(1, n):
        vcopy = v.copy()
        for c in range(C+1):
            if (c-objects[k-1][0]>=0) :
                vcopy[c] = max(v[c], (v[c-objects[k-1][0]] + objects[k-1][1]))
        v = vcopy
    return v[c]  
  
 
objects = [(2, 1), (3, 7), (6, 10), (5, 10), (8, 13), (2, 1), (2, 1)] # chaque objet est un couple (poids, valeur)
print("En stockant toutes les valeurs : ", knapsack1(10, objects)) # knapsack(10, objets) doit renvoyer 18
print("En stockant uniquement les valeurs précédentes : ", knapsack2(10, objects))
