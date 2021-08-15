def czyPalindrom(a):
    b = ""
    for x in range(len(a) // 2):
        b += a[len(a) - x - 1]
    return a == b


parzysta = 0
nieparzysta = 0
with open("hasla.txt", "r") as plik:
    plik = plik.read().split()

    # zadanie a
    for x in plik:
        if len(x) % 2:
            parzysta += 1
        else:
            nieparzysta += 1
    print(parzysta)
    print(nieparzysta)
    print("--------------------")
    # zadanie b
    for x in plik:
        if x == x[::-1]:
            print(x)

    print("--------------------")
    # zadanie c
    for x in plik:
        for y in range(len(x) - 1):
            if ord(x[y]) + ord(x[y + 1]) == 220:
                print(x)
                break
