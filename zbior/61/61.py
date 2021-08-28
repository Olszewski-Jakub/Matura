import math

with open('ciagi.txt') as dane, open('bledne.txt') as bledne, open('odp.txt', 'w') as odp:
    """1 metoda wczytywania danych"""
    dane = dane.readlines()
    bledne = bledne.readlines()
    ciagi = [(dane[x].replace('\n', '')) for x in range(1, len(dane), 2)]
    dlugosc = [dane[x].replace('\n', '') for x in range(0, len(dane), 2)]

    ciagi2 = [(bledne[x].replace('\n', '')) for x in range(1, len(bledne), 2)]

    # print(ciagi, '\n', dlugosc)

    """"2 Metoda wczytywania danychh"""


    # dane = dane.readlines()
    # ciagi, dlugosc = [], []
    # for x in range(len(dane)):
    #     if x % 2 == 0:
    #         dlugosc.append(dane[x].replace('\n', ''))
    #     if x % 2 != 0:
    #         ciagi.append(dane[x].replace('\n', ''))

    def a():
        arr_of_r = []
        count = 0
        for x in ciagi:
            arr = x.split(' ')
            arr = list(map(int, arr))
            r = arr[1] - arr[0]
            czyArytmetycznty = True
            for y in range(1, len(arr) - 1):
                if not (arr[y + 1] - arr[y] == r):
                    czyArytmetycznty = False
            if czyArytmetycznty:
                arr_of_r.append(r)
                count += 1
        print('a) ', count, ' ', max(arr_of_r), file=odp)


    def ifCube(num):
        for x in range(1, 101):
            if (x * x * x) == num:
                return True
        return False


    def b():
        result = []
        for x in ciagi:
            arr = x.split(' ')
            arr = list(map(int, arr))
            for y in range(len(arr)):
                if not ifCube(arr[y]):
                    arr[y] = 0
            if (x := (max(arr))) != 0:
                result.append(x)

        print(
            'b) ', result, file=odp
        )


    def c():
        for x in range(1, len(bledne), 2):
            ciag = bledne[x].split(' ')
            ciag = list(map(int, ciag))
            roznice = []

            for y in range(len(ciag) - 1):
                roznice.append(ciag[y + 1] - ciag[y])


            # check first element
            if roznice[0] != roznice[1] and roznice[1] == roznice[2]:
                print("Błędny wyraz - ", ciag[0])
                continue

            if roznice[0] != roznice[2] and roznice[1] != roznice[2] and roznice[2] == roznice[3]:
                print("Błędny wyraz - ", ciag[1])
                continue


            if roznice[0] == roznice[3] and roznice[0] != roznice[1] and roznice[0] != roznice[2]:
                print("Błędny wyraz - ", ciag[2])
                continue

            for y in range(2,len(roznice)):
                if roznice[0] != roznice[y]:
                    print("Błędny wyraz - ", ciag[y+1])
                    break

    # a()
    # b()
    c()
