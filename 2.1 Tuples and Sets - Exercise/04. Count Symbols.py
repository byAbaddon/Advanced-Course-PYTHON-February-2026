di = {}
for x in input():
    di[x] =  di.setdefault(x, 0) + 1

for k,v in sorted(di.items()):
    print(f'{k}: {v} time/s')