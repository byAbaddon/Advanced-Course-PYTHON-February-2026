lst_o, lst_e = set(), set()

for i, x in enumerate([input() for _ in range(int(input()))], 1):
    r = sum([ord(c) for c in x]) // i
    if r % 10 % 2 == 0:
        lst_e.add(r)
    else:
        lst_o.add(r)

o_sum = sum(lst_o)
e_sum = sum(lst_e)

if e_sum == o_sum:
    res = lst_o.union(lst_e)
elif o_sum > e_sum:
    res = lst_o.difference(lst_e)
else:
    res = lst_o.symmetric_difference(lst_e)

print(', '.join(str(x) for x in res))
