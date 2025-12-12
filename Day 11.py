file = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''.splitlines()

deviceDict = {}

for deviceData in file:
  name = deviceData.split(": ")[0]
  devices = deviceData.split(": ")[1].split(" ")
  deviceDict[name] = devices

print(deviceDict)

def checkDevice(device):
  if deviceDict[device] == ['out']:
    return 1
  else:
    miniSum = 0
    for i in deviceDict[device]:
      miniSum += checkDevice(i)
    return miniSum

print(checkDevice('you'))
