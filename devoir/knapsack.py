def knapsack(capacity, objects):
  # à remplir
  # renvoyer la valeur maximum que l'on peut obtenir en prennant des objets dont le poids total est inférieur à capacity
  
 
objects = [(2, 1), (3, 7), (6, 10), (5, 10), (8, 13), (2, 1), (2, 1)] # chaque objet est un couple (poids, valeur)
assert knapsack(10, objects) == 10 # knapsack(10, objets) doit renvoyer 18
