file = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''.splitlines()

import re
import itertools
import z3

count = 0

for machine in file:
    splits = machine.split(" ")
    diagram = splits[0][1:-1]
    buttons = [x[1:-1] for x in splits[1:-1]]
    voltages = splits[-1][1:-1].split(",")
    finalSchematic = []
    for i in diagram:
        if i == ".":
            finalSchematic.append(0)
        else:
            finalSchematic.append(1)
    notFound = True
    buttonsToSelect = 1
    s = z3.Optimize()
    
    for i in range(0, len(diagram)):
        variables = []
        for buttonNum in range(0, len(buttons)):
            if str(i) in buttons[buttonNum]:
                variables.append(z3.Int('X' + str(buttonNum)))
        s.add(sum(variables) == int(voltages[i]))
        for j in variables:
            s.add(j >= 0)
    possibleVariables = []
    for buttonNum2 in range(0, len(buttons)):
        possibleVariables.append(z3.Int('X' + str(buttonNum2)))
    s.minimize(sum(possibleVariables))
    s.check()
    m = s.model()
    miniSum = 0
    for button in m:
        miniSum += m[button].as_long()
    count += miniSum
print(count)
