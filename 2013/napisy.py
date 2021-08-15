with open("napisy.txt", "r") as plik:
    plik = plik.read().split()


def a():
    conut = 0
    for x in plik:
        if len(x) % 2 != 0:
            conut += 1

    return conut


def b():
    for x in plik:
        if x.count('0') == x.count('1'):
            print(x)


def c():
    count_0 = 0
    count_1 = 0
    for x in plik:
        if x.count('0') == len(x):
            count_0 += 1
        if x.count('1') == len(x):
            count_1 += 1
    print('1', count_1)
    print('0', count_0)


print(a())
b()
c()
