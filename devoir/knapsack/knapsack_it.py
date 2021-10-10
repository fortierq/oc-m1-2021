# Résolution du sac à dos par programmation dynamique, en itératif

def knapsack(C, objects):
    T = [[0]*(len(objects) + 1) for _ in range(C + 1)]
    taken = [-1]*(C+1)

    for k in range(len(objects)):
        w, v = objects[k]
        for c in range(C + 1):
            T[c][k+1] = T[c][k]
            if w <= c:
                T[c][k+1] = max(T[c][k], T[c - w][k] + v)
    
    v = T[C][-1]
    for k in range(len(objects) - 2, -1, -1):
        if v != T[C][k]:
            print(k)
            C -= objects[k][0]
            v -= objects[k][1]

    return T[-1][-1]
 
objects = [(2, 1), (3, 7), (6, 10), (5, 10), (8, 13), (2, 1), (2, 1)] # chaque objet est un couple (poids, valeur)
print(knapsack(10, objects)) # knapsack(10, objets) doit renvoyer 18
