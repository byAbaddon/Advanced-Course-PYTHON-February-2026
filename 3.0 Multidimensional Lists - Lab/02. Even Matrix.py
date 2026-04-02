print([[int(x) for x in input().split(', ') if not int(x) % 2] for _ in range(int(input()))])
