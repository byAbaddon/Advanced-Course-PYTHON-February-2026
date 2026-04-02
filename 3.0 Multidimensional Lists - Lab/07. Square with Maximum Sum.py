row, col = map(int, input().split(', '))
mtx = [list(map(int, input().split(', '))) for _ in range(row)]

best_sum = float('-inf')
best = []

for r in range(row - 1):
    for c in range(col - 1):
        s = mtx[r][c] + mtx[r][c + 1] + mtx[r + 1][c] + mtx[r + 1][c + 1]
        if s > best_sum:
            best_sum = s
            best = [
                [mtx[r][c], mtx[r][c + 1]],
                [mtx[r + 1][c], mtx[r + 1][c + 1]]
            ]

for row in best:
    print(*row)
print(best_sum)
