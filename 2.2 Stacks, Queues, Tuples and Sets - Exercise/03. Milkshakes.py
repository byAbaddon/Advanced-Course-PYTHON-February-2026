lst_c = list(map(int, input().split(', ')))
lst_m = list(map(int, input().split(', ')))
shakes = 0

while True:
    if not lst_c or not lst_m or shakes == 5: break

    c = lst_c.pop()
    m = lst_m.pop(0)

    if c == m:
        shakes += 1
    else:
        if m <= 0:
            lst_c.append(c)
            continue
        if c <= 0:
            lst_m.insert(0, m)
            continue

        lst_m.append(m)
        c -= 5
        lst_c.append(c)

print('Not enough milkshakes.' if shakes < 5 else 'Great! You made all the chocolate milkshakes needed!')
print(f'Chocolate: {", ".join([str(x) for x in lst_c])}' if len(lst_c) > 0 else 'Chocolate: empty')
print(f'Milk: {", ".join([str(x) for x in lst_m])}' if len(lst_m) > 0 else 'Milk: empty')
