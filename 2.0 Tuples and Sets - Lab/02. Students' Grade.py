di = {}
for x in [input() for x in range(int(input()))]:
    n, g = x.split()
    di.setdefault(n, []).append(float(g))

for k, v in di.items():
    print(f'{k} ->', *[f'{x:.2f}' for x in v], f'(avg: {sum(v) / len(v):.2f})')

