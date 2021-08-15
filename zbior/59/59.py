from math import sqrt, ceil


def isPrime(a):
    if a < 2:
        return False
    if a % 2 == 0 and a != 2:
        return False
    for x in range(3, ceil(sqrt(a)) + 1, 2):
        if a % x == 0:
            return False
    return True


def czynniki(a):
    count = 0
    dzielnik = 3
    if a % 2 == 0:
        return False
    while a > 1:
        if a % dzielnik == 0:
            count += 1
        while a % dzielnik == 0:
            a //= dzielnik
        dzielnik += 2

    return count == 3

def czyPalindrom(x):
    return x == x[::-1]


def iloczynCyfr(x):
    a = 1
    while x > 0:
        a *= x%10
        x//=10
    return a

def moc(a):
    c = 0
    while a > 9:
        a = iloczynCyfr(a)
        c+=1
    return c
with open('liczby.txt') as liczby, open('odp.txt', 'w') as odp:
    liczby = liczby.read().split()


    def a():
        c = 0
        for x in liczby:
            if czynniki(int(x)):
                c += 1
        print("a ", c,file=odp)

    def b():
        c=0
        for x in liczby:
            if czyPalindrom(str(int(x) + int(x[::-1]))):
                c += 1
        print("b ", c, file=odp)

    def c():
        dictionary = dict.fromkeys('12345678', 0)
        for x in liczby:
            dictionary[str(moc(int(x)))] += 1
        print("c ", dictionary, file=odp)


    # b()
    c()