lst_a ,lst_b =[set(map(int, input().split())) for _ in range(2)]

for token in [input() for _ in range(int(input()))]:

    if token == 'Check Subset':
        a = set(lst_a)
        b = set(lst_b)
        print("True" if a <= b or b <= a else "False")

    if 'Add' in token:
        if 'First' in token:
            crn = [int(x) for x in token[10:].split()]
            lst_a = lst_a.union(crn)
        else:
            crn = [int(x) for x in token[11:].split()]
            lst_b = lst_b.union(crn)
    if 'Remove' in token:
        if 'First' in token:
            crn = [int(x) for x in token[13:].split()]
            lst_a = lst_a.difference(crn)
        else:
            crn = [int(x) for x in token[14:].split()]
            lst_b = lst_b.difference(crn)

print(*sorted(lst_a), sep=', ')
print(*sorted(lst_b), sep=', ')
