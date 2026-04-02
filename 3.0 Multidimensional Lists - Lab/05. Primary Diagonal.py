mtx = [input().split() for x in range(int(input()))]
print(sum([int(r[i]) for i, r in enumerate(mtx)]))
