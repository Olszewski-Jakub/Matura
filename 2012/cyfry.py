def sumaCyfr(x):
    a = 0
    while x > 0:
        a += x % 10
        x //= 10
    return a


def ciag(n):
    return all(i < j for i, j in zip(n, n[1:]))

def ciagi2(n):
    for i in range(len(n)-1):
        if n[i] >= n[i+1]:
            return False
    return True

with open("cyfry.txt", "r") as plik:
    plik = plik.read().split()

    parzyste = 0
    for x in plik:
        if int(x) % 2 == 0:
            parzyste += 1

    print(parzyste)
    print("------------")
    maximum, minimum = 0, 1000000
    liczbamax, liczbamin = 0, 0
    for x in plik:
        suma = sumaCyfr(int(x))
        if suma > maximum:
            maximum = suma
            liczbamax = x
        if suma < minimum:
            minimum = suma
            liczbamin = x
    print(liczbamax)
    print(liczbamin)
    print("------------")
    c = []
    for x in plik:
        if ciagi2(x):
            c.append(x)
    print(c)
