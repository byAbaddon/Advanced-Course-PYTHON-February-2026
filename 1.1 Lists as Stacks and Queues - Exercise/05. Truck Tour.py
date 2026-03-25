from collections import deque

n = int(input())
pumps = deque()

for i in range(n):
    petrol, dist = map(int, input().split())
    pumps.append((petrol, dist, i))

while True:
    fuel = 0
    success = True

    for petrol, dist, idx in pumps:
        fuel += petrol
        if fuel < dist:
            success = False
            break
        fuel -= dist

    if success:
        print(pumps[0][2])
        break

    pumps.rotate(-1)
