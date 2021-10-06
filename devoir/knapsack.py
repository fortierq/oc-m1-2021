def knapsack(C, objects):
    # à remplir
    # renvoyer la valeur maximum que l'on peut obtenir en prennant des objets dont le poids total est inférieur à C
  n = len(objects)
  v = [[0 for x in range(C + 1)] for y in range(n)]


    for c in range(1, C+1):
        v[c][0] = 0


    for c in range(1, C ):
        for k in (objects):
            if c-objects[k[0]] >= 0:
                v[0][c] = objects[k[0]]

    for i in range(1, n):
        for c in range(1, C):

            if c-k >= 0:
                v[i][c] = max(v[i - 1][c], k + v[i - 1][c - k[0]])


    return v[n - 1][C]

if __name__ == '__main__':
 
    objects = [(2, 1), (3, 7), (6, 10), (5, 10), (8, 13), (2, 1), (2, 1)] # chaque objet est un couple (poids, valeur)
    print(knapsack(10, objects)) # knapsack(10, objets) doit renvoyer 18
