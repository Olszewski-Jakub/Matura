def czyPalindrom(a):
    b = ""
    for x in range(len(a)):
        b += a[len(a) - x - 1]
    return (a == b)


with open("dane.txt", "r") as plik:
    # print(plik.read().split())
    plik = plik.read().split()
    # print(plik.readline().strip())
    # print(plik.readline().strip())
    # print(plik.readline().strip())
    for x in plik:
        if czyPalindrom(x):
            print(x)


