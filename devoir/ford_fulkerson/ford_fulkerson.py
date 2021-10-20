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
#wikipedia pseudoCode implementation
def bfs(G): #parcours en largeur depuis 0 (s)
    s=0
    pred = [-1] * len(G)
    marque=[False for _ in range(len(G))]
    f=[]
    f.insert(0,s)
    marque[s]=True
    while(len(f)!=0):
        s=f[-1]
        del f[-1]
        #print("vertice:{}".format(s))
        for t in range(len(G[s])):
            if(G[s][t]>0 and not(marque[t])):
                f.insert(0,t)
                pred[t]=s
                marque[t]=True
    #print("pred:{}".format(pred))
    if(pred[1]==-1):
        return None
    return pred
#wikipedia pseudoCode implementation
def prim(G):
    s=0
    pred=[-1]*len(G)
    cout=[float("inf")]*len(G)
    cout[s]=0
    F=[i for i in range(len(G)-1,-1,-1)]
    while (len(F)!=0):
        t=F[-1]
        del F[-1]
        for u in range(len(G)):
            if(G[t][u]>0 and (u in F) and cout[u]>=G[t][u]):#si c'est une arrete et l'arrete est meilleur
                pred[u]=t
                cout[u]=G[t][u]
                del F[F.index(u)]
                F.append(u)
        
    #print(pred)
    if(pred[1]==-1):
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
#Comment générer des graph aléatoires ?
#s=0 t=1
#Ensemble d'arretes aléatoires menant de 0 à 1
#Matrice d'adjacence
def dfsHelp(G): # parcours en profondeur depuis 0 (s)
    pred = [-1] * len(G)
    def aux(v, p): # p est le prédecesseur de v
        if pred[v] == -1:
            pred[v] = p
            for w in range(len(G[v])):#on parcours toutes les arretes de v
                if G[v][w] > 0:#si il existe une arrete
                    aux(w, v)#
    aux(0, -1)
    return pred
#Create a random graph complet with size s
#s=0 t =1
def randomGraphMatrix(s):
    G = np.zeros((s, s))
    #rand=lambda x: 0 if x<0.6 else int(random.random()*15)
    for i in range(s):
        for j in range(s):
            if(i==j):
                G[i][j]=0
            else:
                G[i][j]=np.random.randint(low=1,high=20)
    #Connecting 0 to 1 Je ne sais pas si ça marche de remplir au hasard la matrice puis de connecter 0 et 1
    #d=dfsHelp(G)
    #if(d[1]==-1):
    #    #find pred 0
    #    lastS=-1
    #    lastSInterm=lastS
     #   find=0
      #  for _ in range(len(d)):
       #     for i in range(len(d)):
        #        if(d[i]==find):
         #           lastS=i
          #          break
           # if(lastS==lastSInterm):
              #  break
         #   lastSInterm=lastS
       # if(lastS==-1):
        #    G[0][1]=int(random.random()*10)
       # else:
         #   G[lastS][1]=int(random.random()*10)
    return G

################COMPARISON !!!
###0:DFS/1:BFS/2:prim
executionTime=[[] for _ in range(3)]
size=100
step=10
inputSize=[i for i in range(6,size,step)]
dfsR=[]
bfsR=[]
primR=[]
print("Starting to try")
for i in range(6,size,step):
    graph=randomGraphMatrix(i)
    flow=0
    #DFS
    start=time.time()
    flow=ford_fulkerson(graph,dfs)
    end=time.time()
    executionTime[0].append(end-start)
    dfsR.append(flow)
    #BFS
    start=time.time()
    flow=ford_fulkerson(graph,bfs)
    end=time.time()
    executionTime[1].append(end-start)
    bfsR.append(flow)
    #PRIM
    start=time.time()
    flow=ford_fulkerson(graph,prim)
    end=time.time()
    executionTime[2].append(end-start)
    primR.append(flow)
#checking results
print("dfsR:{}".format(dfsR))
print("bfsR:{}".format(bfsR))
print("primR:{}".format(primR))
print("plotting ...")

plt.plot(inputSize,executionTime[0],"-b",label="dfs")
plt.plot(inputSize,executionTime[1],"-r",label="bfs")
plt.plot(inputSize,executionTime[2],"-v",label="prim")
plt.legend(loc="upper left")
plt.xlabel("inputSize",fontsize='13')
plt.ylabel("executionTime",fontsize='13')
plt.show()
