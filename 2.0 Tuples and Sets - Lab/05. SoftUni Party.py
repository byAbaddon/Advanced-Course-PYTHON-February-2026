lst_g = set([input() for x in range(int(input()))])

for g in iter(input, 'END'):
    if g in lst_g:
        lst_g = [x for x in lst_g if x != g]

print(len(lst_g))
v = sorted([x for x in lst_g if x[0].isdigit()])
o = sorted([x for x in lst_g if not x[0].isdigit()])
print('\n'.join((v + o)))
