lst = [x for x in iter(input, 'End')]
w = int(lst.pop(0))
p_lst = []

for x in lst:
    if x == 'Start': break
    p_lst.append(x)

for i, x in enumerate(lst):
    if i <= len(p_lst): continue

    if 'refill' in x:
        w += int(x.split()[1])
        continue

    if w >= int(x):
        w -= int(x)
        print(f'{p_lst.pop(0)} got water')
    else:
        print(f'{p_lst.pop(0)} must wait')

print(f'{w} liters left')
