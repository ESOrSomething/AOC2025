file = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''.splitlines()

corners = []
for coordinates in file:
  corners.append((int(coordinates.split(",")[0]), int(coordinates.split(",")[1])))
  
print(corners)

areas = {}

for a in corners:
  for b in corners:
    a1, a2 = a
    b1, b2 = b
    if a != b and (b, a) not in areas:
        areas[(a, b)] = (abs(a1-b1)+1)*(abs(a2-b2)+1)

sorted_areas = sorted(areas.items(), reverse=True, key=lambda x: x[1])
print(sorted_areas)
print(sorted_areas[0][1])
