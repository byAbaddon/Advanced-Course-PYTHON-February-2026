food = int(input())
lst = [int(x) for x in input().split()]

print(max(lst))

while lst:
    x = lst.pop(0)
    if food >= x:
        food -= x
    else:
        lst.insert(0, x)
        print('Orders left:', *lst)
        exit()

print('Orders complete', *lst)
