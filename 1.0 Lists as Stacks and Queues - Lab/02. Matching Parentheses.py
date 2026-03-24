txt = input()
lst = []

for i, x in enumerate(txt):
    if txt[i] == '(':
        lst.append(i)

    if txt[i] == ')':
        start_index = lst.pop()
        end_index = i
        print(txt[start_index: end_index + 1])