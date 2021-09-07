from math import ceil, sqrt

with open('ciagi.txt') as ciagi, open('odp.txt', 'w') as odp:
    def ifPrime(a):
        if a < 2:
            return False
        if a % 2 == 0 and a != 2:
            return False
        for x in range(3, ceil(sqrt(a)) + 1, 2):
            if a % x == 0:
                return False
        return True


    def DowToDec(num, sys):
        sum = 0
        pot = 1
        for x in str(num)[::-1]:
            sum += int(x) * pot
            pot *= sys
        return sum


    def czy_polpierwsza(num):
        num = int(num)
        for x in range(2, num):
            if num % x == 0 and ifPrime(x) and ifPrime(num // x):
                return True
        return False


    """ 
        Ciągiem dwucyklicznym będziemy nazywać taki ciąg zerojedynkowy w o długości parzystej, 
        który składa się z dwóch fragmentów w1 oraz w2, w = w1w2 takich że w1= w2. Podaj
        wszystkie ciągi dwucykliczne zapisane w pliku ciagi.txt.    
    """
    ciagi = ciagi.read().split()


    def a():
        arr = []
        for x in ciagi:
            if (y := len(x)) % 2 == 0 and x[:y // 2] == x[y // 2::]:
                arr.append(x)
        print("a) ", *arr, file=odp)


    """
        Podaj liczbę ciągów z pliku ciagi.txt, w których nie występują obok siebie dwie jedynki. 
    """


    def b():
        c = 0
        for x in ciagi:
            two_ones = False
            for y in range(len(x) - 1):
                if x[y] == '1' and x[y + 1] == '1':
                    two_ones = True

            if not two_ones:
                c += 1

        print("b) ", c, file=odp)


    """
    Liczbą półpierwszą nazywamy taką liczbę, która jest iloczynem dwóch liczb pierwszych.
    Podaj, ile ciągów z pliku ciagi.txt jest reprezentacją binarną liczb półpierwszych. Dodatkowo podaj największą i najmniejszą liczbę półpierwszą w zapisie dziesiętnym. 
    """


    def c():
        max, min, c = 0, 10000000, 0
        for x in ciagi:
            if czy_polpierwsza((num := DowToDec(x, 2))):
                c += 1
                if (y := int(num)) > max: max = y
                if (y := int(num)) < min: min = y

        print('c) ', c, ' ', max, ' ', min, file=odp)


    a()
    b()
    c()
