from collections import deque

robots_input = input().split(';')
start_time = input()

robots = []
for r in robots_input:
    name, t = r.split('-')
    robots.append([name, int(t), 0])

h, m, s = map(int, start_time.split(':'))
time = h*3600 + m*60 + s

products = deque()
while True:
    x = input()
    if x == "End":
        break
    products.append(x)

while products:
    time += 1
    product = products.popleft()

    for r in robots:
        if r[2] > 0:
            r[2] -= 1

    assigned = False
    for r in robots:
        if r[2] == 0:
            r[2] = r[1]
            hh = (time//3600) % 24
            mm = (time//60) % 60
            ss = time % 60
            print(f"{r[0]} - {product} [{hh:02d}:{mm:02d}:{ss:02d}]")
            assigned = True
            break

    if not assigned:
        products.append(product)
