import pants
import math
import csv
from pprint import pprint

#déclaration des variables
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

#Affichage
pprint(solution.distance)
