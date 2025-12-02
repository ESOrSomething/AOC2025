input = open("input.txt", "r").read().split(',')
count = 0

for r in input:
    startID, endID = r.split('-')
    sc = 0
    ec = 0

    if len(startID) % 2 != 0 and len(endID) % 2 != 0:
        continue
    elif len(startID) % 2 == 0 and len(endID) % 2 == 0:
        sc = startID
        ec = endID
    elif len(endID) % 2 != 0:
        sc = startID
        ec = int(str("9")*len(startID))
    else:
        sc = 10**len(startID)
        ec = endID
    l = int(len(str(sc))/2)
    print(sc)
    halfToCheck = int(str(sc)[:l])

    print("P")

    print(int(str(halfToCheck) * 2))

    if int(str(halfToCheck) * 2) not in range(int(sc), int(ec) + 1):
        halfToCheck += 1
    while int(str(halfToCheck) * 2) in range(int(sc), int(ec) + 1):
        print(int(str(halfToCheck) * 2))
        count += int(str(halfToCheck) * 2)
        halfToCheck += 1

print(count)
    