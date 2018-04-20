import pants
import math
import csv
import matplotlib.pyplot as plt
import networkx as nx
import time
from datetime import timedelta
from pprint import pprint

#déclaration des variables
G = nx.Graph()
nodes = []
max = 20

#Remplissage du tableau avec les données d'open_pubs
with open('open_pubs.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nodes.append((float(row['easting']), float(row['northing'])))

nodes = nodes[0:max]



#Calcule des distances les plus courtes avec la méthode euclidienne
def distance (x,y):
    dist = math.sqrt(pow(x[1]-y[1],2) + pow(x[0]-y[0],2))
    return dist


#Création du monde
monde = pants.World(nodes, distance)
solver = pants.Solver()

#Résolution du monde
solution = solver.solve(monde)

columns = "{!s:<25}\t{:<25}"
divider = "-" * (25 + 25)
header = columns.format("Temps passé", "Distance")
columns = columns.replace('<', '>', 1)

print()
print(header)
print(divider)

fastest = None
start_time = time.time()
for i, ant in enumerate(solver.solutions(monde)):
   fastest = ant
   fastest_time = timedelta(seconds=(time.time() - start_time))
   print(columns.format(fastest_time, ant.distance))
total_time = timedelta(seconds=(time.time() - start_time))

print(divider)
print("Meilleur solution:")
for i, n in zip(fastest.visited, fastest.tour):
   print("  {:>8} = {}".format(i, n))

print("Solution : {}".format(fastest.distance))
print("Trouvé en {} sur {} seconds.".format(fastest_time, total_time))

G.add_nodes_from(nodes)
nx.draw_networkx(G)
plt.show()