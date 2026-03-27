di = {}
for x in  input().split():
    x = float(x)
    di[x] = di.setdefault(x, 0) + 1

for k,v in di.items():
    print(f'{k} - {v} times')