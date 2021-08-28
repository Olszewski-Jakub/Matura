def OsemkowyToDec(num):
    sum = 0
    pot = 1
    for x in str(num)[::-1]:
        sum += (ord(x) - 48) * pot
        pot *= 8
    return sum


def decToOsemkowy(num):
    a = ''
    while num > 0:
        a = str(num % 8) + a
        num //= 8
    return a


with open('liczby1.txt') as liczby1, open('liczby2.txt') as liczby2, open("wyniki.txt", 'w') as odp:
    liczby2 = liczby2.read().split()
    liczby2 = list(map(int, liczby2))

    liczby1 = liczby1.read().split()
    liczby1 = list(map(int, liczby1))


    # print(liczby2)
    # print(type(liczby2[0]))
    def b():
        ciag_len = 1
        ciag_len_max = 0
        p_element = 0
        p_element_max = 0
        for x in range(999):
            if liczby2[x] <= liczby2[x + 1]:
                if ciag_len == 1:
                    p_element = liczby2[x]
                ciag_len += 1
            else:
                print(ciag_len)
                if ciag_len_max < ciag_len:
                    ciag_len_max = ciag_len
                    p_element_max = p_element
                    p_element = 0
                ciag_len = 1
        print("b) ", ciag_len_max, " ", p_element_max, file=odp)


    def b2():
        ciag = []
        max_ciag = []
        for x in range(500):
            if liczby2[x] <= liczby2[x + 1]:
                print(liczby2[x])
                ciag.append((liczby2[x]))
            else:
                print('----------------------')
                ciag.append(liczby2[x])
                if len(ciag) > len(max_ciag):
                    max_ciag = ciag.copy()
                ciag = []
        print(max_ciag)


    def c():
        te_same, wiekszy1 = 0, 0
        for x in range(1000):
            if OsemkowyToDec(liczby1[x]) == liczby2[x]:
                te_same += 1
            if OsemkowyToDec(liczby1[x]) > liczby2[x]:
                wiekszy1 += 1
        print('c) ', te_same, " ", wiekszy1, file=odp)


    # TODO Do domu
    def d():
        dziesietny, osemkowy = 0, 0
        ile_6_dziesietny = "".join(list(map(str, liczby2))).count('6')
        ile_6_osomkowy = "".join(list(map(decToOsemkowy, liczby2))).count('6')
        print('d) ', ile_6_osomkowy, ' ', ile_6_dziesietny, file=odp)


    # b()
    # c()
    d()
