row, col = map(int, input().split(','))
mrx = []
r = 0

for _ in range(row):
    crt = [int(x) for x in input().split(', ')]
    r += sum(crt)
    mrx.append(crt)

print(r,'\n', mrx)