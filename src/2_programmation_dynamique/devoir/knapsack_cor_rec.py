from functools import lru_cache

def knapsack(C, objects):
    @lru_cache(maxsize=None)
    def aux(C, k):
        if k == -1:
            return 0
        if objects[k][0] > C:
            return aux(C, k-1)
        else:
            return max(objects[k][1] + aux(C - objects[k][0], k-1), aux(C, k-1))

    v = aux(C, len(objects)-1)
    for i in range(len(objects)-1, -1, -1):
        if v != aux(C, i-1):
            print(i)
            v -= objects[i][1]
            C -= objects[i][0]
    return

objects = [(2, 1), (3, 7), (6, 10), (5, 10), (8, 13), (2, 1), (2, 1)] # chaque objet est un couple (poids, valeur)
print(knapsack(10, objects)) # knapsack(10, objets) doit renvoyer 18
