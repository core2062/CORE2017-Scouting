
l = [(2, 3), (6, 7), (3, 34), (24, 64), (1, 43)]
def getKey(item):
    return item[1]
l.append((9, 62),)
f = sorted(l, key=getKey)
for item in f:
    print(item)