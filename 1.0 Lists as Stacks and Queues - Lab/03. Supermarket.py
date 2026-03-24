lst = []

for x in iter(input, 'End'):
    lst.append(x)
    if x == 'Paid':
        [print(x) for x in lst[:-1]]
        lst = []

print(len(lst), 'people remaining.')