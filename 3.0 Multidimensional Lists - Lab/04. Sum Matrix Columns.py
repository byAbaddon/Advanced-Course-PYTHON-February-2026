row, col = map(int, input().split(', '))
mtx = [[int(x) for x in input().split()] for x in range(row)]

for c in range(col):
    res = 0
    for r in range(row):
        res +=mtx[r][c]
    print(res)

