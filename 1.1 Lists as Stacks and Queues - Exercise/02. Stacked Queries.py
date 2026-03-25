stk = []

for x in [input() for x in range(int(input()))]:
    if ' ' in x:  # 1
        n = int(x.split()[1])
        stk.insert(0, n)
    if stk:
        if x == '2':
            stk.pop(0)
        if x == '3':
            print(max(stk))
        if x == '4':
            print(min(stk))

print(', '.join([str(x) for x in stk]))
