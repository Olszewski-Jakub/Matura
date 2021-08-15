def binToDec(a):
    sum = 0
    potega = 1
    for x in a[::-1]:
        sum += int(x) * potega
        potega *= 2
    return sum


def decToBin(a):
    b = ''
    while a > 0:
        b = str(a % 2) + b
        a //= 2
    return b


with open('liczby.txt') as liczby, open('zadanie6.txt', 'w') as odp:
    liczby = liczby.read().split()


    def a():
        count = 0
        for x in liczby:
            if x[-1] == '0':
                count += 1
        print("a ",count,file=odp)


    def b():
        mymax = [0, '0']
        for x in liczby:
            a = binToDec(x)
            if a > mymax[0]:
                mymax = [a, x]
        odp.write(f"b {mymax}")


    def c():
        sum = 0
        for x in liczby:
            if len(x) == 9:
                sum += binToDec(x)
        print("c ", sum, decToBin(sum), file=odp)


    a()
    b()
    c()
