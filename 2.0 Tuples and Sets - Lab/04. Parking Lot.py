lst = []

for x in [input() for x in range(int(input()))]:
    c, n = x.split(', ')
    if c == 'IN':
        if n not in lst:
            lst.append(n)
    if c == 'OUT':
        lst = [x for x in lst if x != n]

if lst:
    [print(x) for x in lst]
else:
    print('Parking Lot is Empty')