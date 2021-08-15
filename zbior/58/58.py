from math import ceil

def DowToDec(num, sys):
    sum = 0
    pot = 1
    for x in str(num)[::-1]:
        sum += int(x) * pot
        pot *= sys
    return sum

def decToDow(num, sys):
    a = ""
    while num > 0:
        a = str(num % sys) + a
        num //= sys
    return a


with open('dane_systemy1.txt') as s1, open('dane_systemy2.txt') as s2, open('dane_systemy3.txt') as s3, \
        open('odp.txt', 'w') as odp:
    s1 = s1.read().split()
    for x in range(len(s1)):
        if not str(s1[x])[0] == "-":
            s1[x] = DowToDec(int(s1[x]), 2)
        else:
            s1[x] = DowToDec(int(s1[x].replace("-", "")), 2) * (-1)

    s2 = s2.read().split()
    for x in range(len(s2)):
        if not str(s2[x])[0] == "-":
            s2[x] = DowToDec(int(s2[x]), 4)
        else:
            s2[x] = DowToDec(int(s2[x].replace("-", "")), 4) * (-1)

    s3 = s3.read().split()
    for x in range(len(s3)):
        if not str(s3[x])[0] == "-":
            s3[x] = DowToDec(int(s3[x]), 8)
        else:
            s3[x] = DowToDec(int(s3[x].replace("-", "")), 8) * (-1)


    def a():
        arr = [10000000000, 10000000000, 10000000000]
        for x in s1:
            if int(x) < arr[0]:
                arr[0] = int(x)
        for x in s2:
            if int(x) < arr[1]:
                arr[1] = int(x)
        for x in s3:
            if int(x) < arr[2]:
                arr[2] = int(x)
        arr[0] = "-" + decToDow(int(str(arr[0]).replace("-","")),2)
        arr[1] = "-" + decToDow(int(str(arr[1]).replace("-","")),2)
        arr[2] = "-" + decToDow(int(str(arr[2]).replace("-","")),2)
        odp.write(f"a{arr}")

    def b():
        h = 12
        count = 0
        for x in range(0,1095*2,2):
            if s1[x]!= h and s2[x]!= h and s3[x] != h:
                count += 1
            h+=24
        odp.write(f"\nb {count}")

    def c():
        count = 1
        rek = [s1[1],s2[1],s3[1]]
        for x in range(3,1095*2,2):
            if s1[x] > rek[0] or s2[x] > rek[1] or s3[x] > rek[2]:
                count += 1
            if s1[x] > rek[0]:
                rek[0] = s1[x]
            if s2[x] > rek[1]:
                rek[1] = s2[x]
            if s3[x] > rek[2]:
                rek[2] = s3[x]
        odp.write(f"\nc{count}")

    def d():
        max_skok = 0
        for x in range(1,1095*2,2):
            for y in range(1, 1095 * 2, 2):
                r_i_j = (int(s1[x]) - int(s1[y]))**2
                i_j = abs(x/2-y/2)
                if i_j>0:
                    skok = ceil(int(r_i_j)/int(i_j))
                    if skok > max_skok:
                        max_skok = skok
        odp.write(f"\nd {max_skok}")

    a()
    b()
    c()
    d()
