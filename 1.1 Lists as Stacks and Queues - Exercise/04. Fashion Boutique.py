lst = [int(x) for x in input().split()]
CAP = int(input())
crt = CAP
count = 1

while lst:
    x = lst.pop(0)

    if crt == x:
        if lst:
            count += 1
            crt = CAP
    elif x > crt:
        lst.insert(0, x)
        count += 1
        crt = CAP
    else:
        crt -= x

print(count)
