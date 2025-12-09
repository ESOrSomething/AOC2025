import networkx as nx
import re
import math
import matplotlib.pyplot as plt

file = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''.splitlines()

coords = []

G = nx.Graph()

for line in file:
  coordsToAppend = [int(x) for x in re.findall(r'\d+', line)]
  coords.append((coordsToAppend[0], coordsToAppend[1], coordsToAppend[2]))

distances = {}

for a in coords:
  for b in coords:
    a1, a2, a3 = a
    b1, b2, b3 = b
    if ((b1, b2, b3), (a1, a2, a3)) not in distances and a != b:
      distances[((a1, a2, a3), (b1, b2, b3))] = math.sqrt((a1 - b1)**2 + (a2 - b2)**2 + (a3 - b3)**2)

sorted_items = sorted(distances.items(), key=lambda item: item[1])
for i in range(0, 1000):
  G.add_edge(*sorted_items[i][0])

nx.draw(G)

print([
    len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)
][:3])

product = 1
for i in [
    len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)
][:3]:
  product *= i

print(product)
plt.show()
