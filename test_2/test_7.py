
countS = 0
countH = 0
countE = 0
countR = 0
countI = 0
countF = 0
min_in_mass_s = 0


s = str(input())

def serchSim(i):
    count = 0
    start = -1
    while True:
        start = s.find(i, start+1)
        if start == -1:
            break
        count += 1
    return count

countF = serchSim('f')

countF_s = countF // 2
s_counte = [serchSim('s'), serchSim('e'), serchSim('h'), serchSim('r'), serchSim('i')]
min_in_mass_s =  min(s_counte)

if countF < 2 or min_in_mass_s == 0:
    print(0)
else:
    cc = min_in_mass_s
    for i in range(min_in_mass_s+1):
        if cc <= countF_s:
            print(cc)
            break
        else: cc-1 