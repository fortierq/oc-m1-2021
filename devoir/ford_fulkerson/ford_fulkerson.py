import numpy as np

G = np.zeros((6, 6))
G[0][2] = 7
G[2][3] = 2
G[3][1] = 1
G
def cmin(G, pred): # renvoie la capacité min le long du chemin pred
    mini = float("inf")
    v = 1 # correspond au sommet t
    while v != 0: # tant que je ne suis pas revenu sur 0
        mini = min(mini, G[pred[v]][v])
        v = pred[v]
    return mini

def dfs(G): # parcours en profondeur depuis 0 (s)
    pred = [-1] * len(G)
    def aux(v, p): # p est le prédecesseur de v
        print(v)
        if pred[v] == -1:
            pred[v] = p
            for w in range(len(G[v])):
                if G[v][w] > 0:
                    aux(w, v)
    aux(0, -1)
    print(pred)
    if pred[1] == -1:
        return None
    return pred
                           
def ford_fulkerson(G, path): 
    # path(G) renvoie un chemin sous forme d'un tableau de prédécesseurs pred
    # pred[1] = sommet prédecesseur du sommet 1 dans un chemin de 0 à 1 
    # path(G) renvoie None s'il n'y a pas de chemin de 0 à 1
    flow = 0
    while (pred := path(G)) is not None:
        mini = cmin(G, pred)
        print(mini)
        v = 1 # correspond au sommet t
        while v != 0: # tant que je ne suis pas revenu sur 0
            G[pred[v]][v] -= mini
            G[v][pred[v]] += mini
            v = pred[v]
        flow += mini
    return flow
