file = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''.splitlines()

import re
import itertools

count = 0

for machine in file:
  splits = machine.split(" ")
  diagram = splits[0][1:-1]
  buttons = [x[1:-1] for x in splits[1:-1]]
  finalSchematic = []
  for i in diagram:
    if i == ".":
      finalSchematic.append(0)
    else:
      finalSchematic.append(1)
  notFound = True
  buttonsToSelect = 1
  while notFound:
    for selectedButtons in itertools.combinations(buttons, buttonsToSelect):
      schematic = []
      for i in diagram:
        schematic.append(0)
      for button in selectedButtons:
        for press in button.split(","):
          schematic[int(press)] = (schematic[int(press)] + 1) % 2 
      if schematic == finalSchematic and notFound:
          count += buttonsToSelect
          notFound = False
    buttonsToSelect += 1
print(count)
