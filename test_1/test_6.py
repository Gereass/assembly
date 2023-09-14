s = 0
n = 0
a = []
k = 0

n, s = map(int, input().split())
a = [int(i) for i in input().split()]
a = sorted(a)
a.reverse()

for i in a:
    if s < i:
        k = 0
    elif s >= i:
        k = i
        break

print(k)
