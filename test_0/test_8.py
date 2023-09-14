
import itertools as it 

n = 0
m = 0
r = 0
a = []

n, m = map(int, input().split())
a = [int(i) for i in input().split()]

def filtrBaxs():
    j = []
    for i in a:
        if i <= n:
            j.append(i)
            j.append(i)
    j.sort()
    return(j)

def coinChange(b, a):
    for i in range(1, len(a) + 1):
        comb = it.combinations(a, i)
        for j in comb:
            if sum(j) == b:
                return(j)

a = filtrBaxs()
r =  coinChange(n,a)
print(-1 if r == None else r)