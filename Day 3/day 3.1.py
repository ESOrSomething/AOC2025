input = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

import itertools

count = 0

print("WORKS")

for line in input:
  maxNum = 0
  for i in range(len(line)):
     for j in range(len(line)):
        if i < j and int(line[i]+line[j]) > maxNum:
            maxNum = int(line[i]+line[j])
  count += maxNum
print(count)