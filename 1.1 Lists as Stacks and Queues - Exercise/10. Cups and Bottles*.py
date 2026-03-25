cups_list, bottle_list = [list(map(int, input().split())) for x in range(2)]
wasted_water = 0

while cups_list and bottle_list:
    cup = cups_list[0]
    bottle = bottle_list.pop()

    if cup > bottle:
        while cup > 0:
            if bottle < cup:
                cup -= bottle
                bottle = bottle_list.pop()
            else:
                bottle -= cup
                cup = 0
    wasted_water += abs(bottle - cup)
    cup = cups_list.pop(0)

if cups_list:
    print('Cups:', *cups_list, f'\nWasted litters of water: {wasted_water}')
else:
    print(f'Bottles:', *bottle_list, f'\nWasted litters of water: {wasted_water}')