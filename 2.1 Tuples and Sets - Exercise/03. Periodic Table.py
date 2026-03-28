lst = [input().split() for x in range(int(input()))]
print('\n'.join(set().union(*lst)))
