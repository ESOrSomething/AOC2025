file = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()

count = 0
lock = 50

for line in file:
    if line[0] == "L":
        lock = (lock - int(line[1:])) % 100
    else:
        lock = (lock + int(line[1:])) % 100
    print(lock)
    if lock == 0:
        count += 1

print(count)