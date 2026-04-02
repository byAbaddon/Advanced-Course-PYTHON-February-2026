mtx = [[x for x in input()] for _ in range(int(input()))]
syb = input()

for r in range(len(mtx)):
    for c in range(len(mtx)):
        if mtx[r][c] == syb:
            print(f'({r}, {c})')
            exit()

print(f'{syb} does not occur in the matrix')
