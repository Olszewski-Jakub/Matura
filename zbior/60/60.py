def nwd(a, b):
    return nwd(b, a % b) if b else a


with open('liczby.txt') as liczby, open('wyniki.txt', 'w') as opd:
    liczby = liczby.read().split()
    liczby = list(map(int, liczby))


    def a():
        l1, l2, c = 0, 0, 0
        for x in liczby:
            if x < 1000:
                l1 = l2
                l2 = x
                c += 1
        print('a) ', c, " ", l1, " ", l2, file=opd)


    def b():
        print('b)',file=opd)
        for x in liczby:
            dzielniki = []
            for y in range(1,x+1):
                if x % y == 0:
                    dzielniki.append(y)
            if len(dzielniki) == 18:
                print(x," - ",*dzielniki, file=opd)

    def c():
        arr = []
        for x in range(len(liczby)):
            temp = True
            for y in range(len(liczby)):
                if liczby[x] != liczby[y]:
                    if nwd(liczby[x], liczby[y]) > 1:
                        temp = False
                        break
            if temp:
                arr.append(liczby[x])
        print("c ",max(arr),file=opd)


    # print(nwd(25,75))
    a()
    b()
    c()
