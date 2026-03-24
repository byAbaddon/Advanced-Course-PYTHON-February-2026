lst_p, n = input().split(), int(input())

while len(lst_p) > 1:
    for i in range(1, n):
        lst_p.append(lst_p.pop(0))
    else:
        print('Removed', lst_p.pop(0))

print('Last is', *lst_p)