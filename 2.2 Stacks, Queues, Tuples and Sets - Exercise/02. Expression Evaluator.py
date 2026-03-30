from math import trunc

r = ''
for crt in input().split():
    if crt not in ['-', '+', '/', '*']:
        r += crt + ' '
    else:
        r = r.replace(' ', crt)[:-1]
        r = str(trunc(eval(r))) + ' '

print(r)

