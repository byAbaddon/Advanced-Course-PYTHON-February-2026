ar, br = input().split()

a = [input() for _ in range(int(ar))]
b = [input() for _ in range(int(br))]

print('\n'.join(set(a) & set(b)))

