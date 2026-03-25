green_light, yellow_light = int(input()), int(input())
total_time = green_light + yellow_light
passed_cars = 0
waiting_cars_list = []

for car in [x for x in iter(input, 'END')]:
    current_time = 0
    if car != 'green':
        waiting_cars_list.append(car)
    else:
        while waiting_cars_list and green_light > current_time:
            passed_cars += 1
            waiting_car = waiting_cars_list.pop(0)
            for char in waiting_car:
                current_time += 1
                if current_time > total_time:
                    print(f'A crash happened!\n{waiting_car} was hit at {char}.')
                    exit()

print(f'Everyone is safe.\n{passed_cars} total cars passed the crossroads.')